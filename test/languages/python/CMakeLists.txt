if (PYTHON)
    # make a virtualenv to install our generated whl file into
    set(venv_path ${CMAKE_BINARY_DIR}/venv)
    add_custom_command(COMMAND virtualenv ${venv_path}
                       COMMAND ${venv_path}/bin/pip install ${CMAKE_BINARY_DIR}/src/languages/python/setup/dist/*.whl
                       COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_CURRENT_BINARY_DIR}/pip-installed
                       OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/pip-installed
                       )
    add_custom_target(pip_install DEPENDS pip-installed)
    add_dependencies(pip_install pyfoobar)

    # run the tests within the virtualenv
    add_test(PythonTestsVirtualEnv
             ${venv_path}/bin/python ${CMAKE_CURRENT_SOURCE_DIR}/test.py
             )

    # run the tests directly on the python lib via PYTHONPATH
    add_test(PythonTestsDirect
             ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test.py
             )
    set_tests_properties(PythonTestsDirect PROPERTIES ENVIRONMENT "PYTHONPATH=${CMAKE_BINARY_DIR}/src/languages/python")

    add_dependencies(check pip_install)
endif()
