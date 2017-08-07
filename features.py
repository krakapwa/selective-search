#!/usr/bin/env python
# -*- np -*-

import collections
import math
import numpy as np
import skimage
import skimage.filters
import scipy.ndimage.filters

SimilarityMask = collections.namedtuple("SimilarityMask", ["size", "color", "texture", "fill","desc"])

class Features:
    def __init__(self, image, label, n_region, similarity_weight = SimilarityMask(1, 1, 1, 1, 1), desc_arr = None, desc_var = 0):
        self.image = image
        self.label = label
        self.w     = similarity_weight

        self.imsize  = float(label.shape[0] * label.shape[1])
        self.size    = self.__init_size(n_region)
        self.color   = self.__init_color(n_region)
        self.bbox    = self.__init_bounding_box(n_region)
        self.texture = self.__init_texture(n_region)
        #self.desc = self.__init_desc(n_region, desc_arr)

    def __init_size(self, n_region):
        bincnt = np.bincount(self.label.ravel(), minlength = n_region)
        return {i : bincnt[i] for i in range(n_region)}

    def __init_color(self, n_region):
        n_bin = 25
        bin_width = int(math.ceil(255.0 / n_bin))

        bins_color = [i * bin_width for i in range(n_bin + 1)]
        bins_label = range(n_region + 1)
        bins = [bins_label, bins_color]

        r_hist = np.histogram2d(self.label.ravel(), self.image[:, :, 0].ravel(), bins=bins)[0] #shape=(n_region, n_bin)
        g_hist = np.histogram2d(self.label.ravel(), self.image[:, :, 1].ravel(), bins=bins)[0]
        b_hist = np.histogram2d(self.label.ravel(), self.image[:, :, 2].ravel(), bins=bins)[0]
        hist = np.hstack([r_hist, g_hist, b_hist])
        l1_norm = np.sum(hist, axis = 1).reshape((n_region, 1))

        hist = np.nan_to_num(hist / l1_norm)
        return {i : hist[i] for i in range(n_region)}

    def __init_bounding_box(self, n_region):
        bbox = dict()
        for region in range(n_region):
            I, J = np.where(self.label == region)
            bbox[region] = (min(I), min(J), max(I), max(J))
        return bbox

    def __init_desc(self, n_region, desc_arr):
        ar = desc_arr
        return {i : ar[i] for i in range(n_region)}

    def __init_texture(self, n_region):
        ar = np.ndarray((n_region, 240))
        return {i : ar[i] for i in range(n_region)}

    def __calc_gradient_histogram(self, label, gaussian, n_region, nbins_orientation = 8, nbins_inten = 10):
        op = np.array([[-1, 0, 1]], dtype=np.float32)
        h = scipy.ndimage.filters.convolve(gaussian, op)
        v = scipy.ndimage.filters.convolve(gaussian, op.transpose())
        g = np.arctan2(v, h)

        # define each axis for texture histogram
        bin_width = 2 * math.pi / 8
        bins_label = range(n_region + 1)
        bins_angle = np.linspace(-math.pi, math.pi, nbins_orientation + 1)
        bins_inten = np.linspace(.0, 1., nbins_inten + 1)
        bins = [bins_label, bins_angle, bins_inten]

        # calculate 3 dimensional histogram
        ar = np.vstack([label.ravel(), g.ravel(), gaussian.ravel()]).transpose()
        hist = np.histogramdd(ar, bins=bins)[0]

        # orientation_wise intensity histograms are serialized for each region
        return np.reshape(hist, (n_region, nbins_orientation * nbins_inten))

    def __init_texture(self, n_region):
        gaussian = skimage.filters.gaussian(self.image, sigma=1.0, multichannel=True).astype(np.float32)
        r_hist = self.__calc_gradient_histogram(
            self.label, gaussian[:, :, 0], n_region
        )
        g_hist = self.__calc_gradient_histogram(
            self.label, gaussian[:, :, 1], n_region
        )
        b_hist = self.__calc_gradient_histogram(
            self.label, gaussian[:, :, 2], n_region
        )

        hist = np.hstack([r_hist, g_hist, b_hist])
        l1_norm = np.sum(hist, axis=1).reshape((n_region, 1))

        hist = np.nan_to_num(hist / l1_norm)
        return {i : hist[i] for i in range(n_region)}

    def __sim_desc(self, i, j):
        #return 1. - (self.desc[i] + self.desc[j])
        return np.exp(-np.linalg.norm(self.desc[i]-self.desc[j])**2)
    

    def __sim_size(self, i, j):
        return 1. - (self.size[i] + self.size[j]) / self.imsize

    def __calc_histogram_intersection(self, vec1, vec2):
        return np.sum(np.minimum(vec1, vec2))

    def __sim_texture(self, i, j):
        return self.__calc_histogram_intersection(self.texture[i], self.texture[j])

    def __sim_color(self, i, j):
        return self.__calc_histogram_intersection(self.color[i], self.color[j])

    def __sim_fill(self, i, j):
        (bi0, bi1, bi2, bi3), (bj0, bj1, bj2, bj3) = self.bbox[i], self.bbox[j]
        (bij0, bij1, bij2, bij3) = min(bi0, bj0), min(bi1, bj1), max(bi2, bj2), max(bi3, bj3)
        bij_size = (bij2 - bij0) * (bij3 - bij1)
        return 1. - (bij_size - self.size[i] - self.size[j]) / self.imsize

    def similarity(self, i, j):
        return self.w.size * self.__sim_size(i, j) + \
               self.w.texture * self.__sim_texture(i, j) + \
               self.w.color * self.__sim_color(i, j) + \
               self.w.fill * self.__sim_fill(i, j)


    def __merge_size(self, i, j, new_region_id):
        self.size[new_region_id] = self.size[i] + self.size[j]

    def __histogram_merge(self, vec1, vec2, w1, w2):
        return (w1 * vec1 + w2 * vec2) / (w1 + w2)

    def __merge_desc(self, i, j, new_region_id):
        self.desc[new_region_id] = np.mean((self.desc[i],self.desc[j]),axis=0)
        #self.color[new_region_id] = self.__histogram_merge(self.color[i], self.color[j], self.size[i], self.size[j])

    def __merge_color(self, i, j, new_region_id):
        self.color[new_region_id] = self.__histogram_merge(self.color[i], self.color[j], self.size[i], self.size[j])

    def __merge_texture(self, i, j, new_region_id):
        self.texture[new_region_id] = self.__histogram_merge(self.texture[i], self.texture[j], self.size[i], self.size[j])

    def __merge_bbox(self, i, j, new_region_id):
        (bi0, bi1, bi2, bi3), (bj0, bj1, bj2, bj3) = self.bbox[i], self.bbox[j]
        self.bbox[new_region_id] = (min(bi0, bj0), min(bi1, bj1), max(bi2, bj2), max(bi3, bj3))

    def merge(self, i, j):
        new_region_id = len(self.size)
        self.__merge_size(i, j, new_region_id)
        self.__merge_color(i, j, new_region_id)
        self.__merge_texture(i, j, new_region_id)
        self.__merge_bbox(i, j, new_region_id)
        #self.__merge_desc(i, j, new_region_id)
        return new_region_id

