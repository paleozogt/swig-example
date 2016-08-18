cmake_minimum_required(VERSION 3.0.1)
include(utils.cmake)

project(foobar)

setup_swig()
setup_python()

add_subdirectory(src)
