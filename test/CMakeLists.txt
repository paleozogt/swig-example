add_subdirectory(languages/python)

# 'make test' isn't good enough
add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND} -V)
