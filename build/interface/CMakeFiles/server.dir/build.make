# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/wqh/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/wqh/catkin_ws/build

# Include any dependencies generated for this target.
include interface/CMakeFiles/server.dir/depend.make

# Include the progress variables for this target.
include interface/CMakeFiles/server.dir/progress.make

# Include the compile flags for this target's objects.
include interface/CMakeFiles/server.dir/flags.make

interface/CMakeFiles/server.dir/src/server.cpp.o: interface/CMakeFiles/server.dir/flags.make
interface/CMakeFiles/server.dir/src/server.cpp.o: /home/wqh/catkin_ws/src/interface/src/server.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/wqh/catkin_ws/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object interface/CMakeFiles/server.dir/src/server.cpp.o"
	cd /home/wqh/catkin_ws/build/interface && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/server.dir/src/server.cpp.o -c /home/wqh/catkin_ws/src/interface/src/server.cpp

interface/CMakeFiles/server.dir/src/server.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/server.dir/src/server.cpp.i"
	cd /home/wqh/catkin_ws/build/interface && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/wqh/catkin_ws/src/interface/src/server.cpp > CMakeFiles/server.dir/src/server.cpp.i

interface/CMakeFiles/server.dir/src/server.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/server.dir/src/server.cpp.s"
	cd /home/wqh/catkin_ws/build/interface && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/wqh/catkin_ws/src/interface/src/server.cpp -o CMakeFiles/server.dir/src/server.cpp.s

interface/CMakeFiles/server.dir/src/server.cpp.o.requires:
.PHONY : interface/CMakeFiles/server.dir/src/server.cpp.o.requires

interface/CMakeFiles/server.dir/src/server.cpp.o.provides: interface/CMakeFiles/server.dir/src/server.cpp.o.requires
	$(MAKE) -f interface/CMakeFiles/server.dir/build.make interface/CMakeFiles/server.dir/src/server.cpp.o.provides.build
.PHONY : interface/CMakeFiles/server.dir/src/server.cpp.o.provides

interface/CMakeFiles/server.dir/src/server.cpp.o.provides.build: interface/CMakeFiles/server.dir/src/server.cpp.o

# Object files for target server
server_OBJECTS = \
"CMakeFiles/server.dir/src/server.cpp.o"

# External object files for target server
server_EXTERNAL_OBJECTS =

/home/wqh/catkin_ws/devel/lib/interface/server: interface/CMakeFiles/server.dir/src/server.cpp.o
/home/wqh/catkin_ws/devel/lib/interface/server: /opt/ros/hydro/lib/libroscpp.so
/home/wqh/catkin_ws/devel/lib/interface/server: /usr/lib/libboost_signals-mt.so
/home/wqh/catkin_ws/devel/lib/interface/server: /usr/lib/libboost_filesystem-mt.so
/home/wqh/catkin_ws/devel/lib/interface/server: /opt/ros/hydro/lib/librosconsole.so
/home/wqh/catkin_ws/devel/lib/interface/server: /opt/ros/hydro/lib/librosconsole_log4cxx.so
/home/wqh/catkin_ws/devel/lib/interface/server: /opt/ros/hydro/lib/librosconsole_backend_interface.so
/home/wqh/catkin_ws/devel/lib/interface/server: /usr/lib/liblog4cxx.so
/home/wqh/catkin_ws/devel/lib/interface/server: /usr/lib/libboost_regex-mt.so
/home/wqh/catkin_ws/devel/lib/interface/server: /opt/ros/hydro/lib/libxmlrpcpp.so
/home/wqh/catkin_ws/devel/lib/interface/server: /opt/ros/hydro/lib/libroscpp_serialization.so
/home/wqh/catkin_ws/devel/lib/interface/server: /opt/ros/hydro/lib/librostime.so
/home/wqh/catkin_ws/devel/lib/interface/server: /usr/lib/libboost_date_time-mt.so
/home/wqh/catkin_ws/devel/lib/interface/server: /usr/lib/libboost_system-mt.so
/home/wqh/catkin_ws/devel/lib/interface/server: /usr/lib/libboost_thread-mt.so
/home/wqh/catkin_ws/devel/lib/interface/server: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/wqh/catkin_ws/devel/lib/interface/server: /opt/ros/hydro/lib/libcpp_common.so
/home/wqh/catkin_ws/devel/lib/interface/server: /opt/ros/hydro/lib/libconsole_bridge.so
/home/wqh/catkin_ws/devel/lib/interface/server: interface/CMakeFiles/server.dir/build.make
/home/wqh/catkin_ws/devel/lib/interface/server: interface/CMakeFiles/server.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable /home/wqh/catkin_ws/devel/lib/interface/server"
	cd /home/wqh/catkin_ws/build/interface && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/server.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
interface/CMakeFiles/server.dir/build: /home/wqh/catkin_ws/devel/lib/interface/server
.PHONY : interface/CMakeFiles/server.dir/build

interface/CMakeFiles/server.dir/requires: interface/CMakeFiles/server.dir/src/server.cpp.o.requires
.PHONY : interface/CMakeFiles/server.dir/requires

interface/CMakeFiles/server.dir/clean:
	cd /home/wqh/catkin_ws/build/interface && $(CMAKE_COMMAND) -P CMakeFiles/server.dir/cmake_clean.cmake
.PHONY : interface/CMakeFiles/server.dir/clean

interface/CMakeFiles/server.dir/depend:
	cd /home/wqh/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wqh/catkin_ws/src /home/wqh/catkin_ws/src/interface /home/wqh/catkin_ws/build /home/wqh/catkin_ws/build/interface /home/wqh/catkin_ws/build/interface/CMakeFiles/server.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : interface/CMakeFiles/server.dir/depend

