if (PYTHON)
    add_test(PythonTests
             ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test.py
             )
    set_tests_properties(PythonTests PROPERTIES ENVIRONMENT "PYTHONPATH=${CMAKE_BINARY_DIR}/src/languages/python")
    add_custom_target(pycheck COMMAND ${CMAKE_CTEST_COMMAND} -R Py*)
    add_dependencies(pycheck pyfoobar)
endif()
