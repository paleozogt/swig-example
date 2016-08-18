cmake_minimum_required(VERSION 3.0.1)
include(utils.cmake)

project(foobar)

if (UNIX)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
endif()

enable_testing()
setup_swig()
setup_python()

add_subdirectory(src)
add_subdirectory(test)
