#!/usr/bin/env python
""" Setup utility for the selective_search package. """

from distutils.core import setup

setup(
    name='selectivesearch',
    version='1.0',
    description='Selective search.',
    install_requires=[
        "Cython>=0.22",
        "joblib>=0.8.4",
        "matplotlib>=1.4.3",
        "numpy>=1.9.2",
        "Pillow>=2.8.1",
        "PyYAML>=3.11",
        "scikit-image>=0.11.3",
        "scikit-learn>=0.16.0",
        "scipy>=0.15.1",
        "pytest>=2.7.0"
        ]
)


