if (PYTHON)
    if (WIN32)
        set(PYLIB_SUFFIX .pyd)
    else()
        set(PYLIB_SUFFIX .so)
    endif()

    # configure the setup stuff
    set(PYTHON_PACKAGE ${CMAKE_PROJECT_NAME})
    set(LIBNAME _${CMAKE_PROJECT_NAME}${PYLIB_SUFFIX})
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/setup.py ${CMAKE_CURRENT_BINARY_DIR}/setup/setup.py)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/MANIFEST.in ${CMAKE_CURRENT_BINARY_DIR}/setup/MANIFEST.in)

    # swig
    set_source_files_properties(../Foobar.i PROPERTIES CPLUSPLUS ON)
    set_property(SOURCE ../Foobar.i PROPERTY SWIG_FLAGS
                 ${swig_extra_flags}
                 -Wall)
    swig_add_module(pyfoobar python ../Foobar.i)
    swig_link_libraries(pyfoobar)
    set_target_properties(_pyfoobar PROPERTIES 
                          OUTPUT_NAME "_${CMAKE_PROJECT_NAME}"
                          SUFFIX ${PYLIB_SUFFIX}
                          COMPILE_FLAGS ${PYTHON_CFLAGS}
                          LINK_FLAGS ${PYTHON_LDFLAGS})
    target_link_libraries(_pyfoobar foobar)
    add_custom_command(TARGET _pyfoobar POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_PROJECT_NAME}.py ${CMAKE_CURRENT_BINARY_DIR}/setup/${PYTHON_PACKAGE}/__init__.py
        COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:_pyfoobar> ${CMAKE_CURRENT_BINARY_DIR}/setup/${PYTHON_PACKAGE}
        COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/setup/setup.py bdist_wheel
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/setup
    )
    add_custom_target(pyfoobar DEPENDS _pyfoobar)

    install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/setup/dist/ DESTINATION lib/python)
endif()
