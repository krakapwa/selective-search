# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.7

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63

# Include any dependencies generated for this target.
include CMakeFiles/segment.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/segment.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/segment.dir/flags.make

CMakeFiles/segment.dir/segment_py.cpp.o: CMakeFiles/segment.dir/flags.make
CMakeFiles/segment.dir/segment_py.cpp.o: segment_py.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/laurent.lejeune/Documents/selective_search_py-boost_v1.63/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/segment.dir/segment_py.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/segment.dir/segment_py.cpp.o -c /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63/segment_py.cpp

CMakeFiles/segment.dir/segment_py.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/segment.dir/segment_py.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63/segment_py.cpp > CMakeFiles/segment.dir/segment_py.cpp.i

CMakeFiles/segment.dir/segment_py.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/segment.dir/segment_py.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63/segment_py.cpp -o CMakeFiles/segment.dir/segment_py.cpp.s

CMakeFiles/segment.dir/segment_py.cpp.o.requires:

.PHONY : CMakeFiles/segment.dir/segment_py.cpp.o.requires

CMakeFiles/segment.dir/segment_py.cpp.o.provides: CMakeFiles/segment.dir/segment_py.cpp.o.requires
	$(MAKE) -f CMakeFiles/segment.dir/build.make CMakeFiles/segment.dir/segment_py.cpp.o.provides.build
.PHONY : CMakeFiles/segment.dir/segment_py.cpp.o.provides

CMakeFiles/segment.dir/segment_py.cpp.o.provides.build: CMakeFiles/segment.dir/segment_py.cpp.o


# Object files for target segment
segment_OBJECTS = \
"CMakeFiles/segment.dir/segment_py.cpp.o"

# External object files for target segment
segment_EXTERNAL_OBJECTS =

segment.so: CMakeFiles/segment.dir/segment_py.cpp.o
segment.so: CMakeFiles/segment.dir/build.make
segment.so: /usr/local/lib/libboost_python3.so
segment.so: /usr/local/lib/libboost_numpy.so
segment.so: /usr/lib/x86_64-linux-gnu/libpython3.5m.so
segment.so: CMakeFiles/segment.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/laurent.lejeune/Documents/selective_search_py-boost_v1.63/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library segment.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/segment.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/segment.dir/build: segment.so

.PHONY : CMakeFiles/segment.dir/build

CMakeFiles/segment.dir/requires: CMakeFiles/segment.dir/segment_py.cpp.o.requires

.PHONY : CMakeFiles/segment.dir/requires

CMakeFiles/segment.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/segment.dir/cmake_clean.cmake
.PHONY : CMakeFiles/segment.dir/clean

CMakeFiles/segment.dir/depend:
	cd /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63 /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63 /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63 /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63 /home/laurent.lejeune/Documents/selective_search_py-boost_v1.63/CMakeFiles/segment.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/segment.dir/depend
