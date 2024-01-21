# This Cmake module provides two public functions:
#
# litgen_find_pybind11()
# **************************************************************
# litgen_find_pybind11() will find pybind11, and is equivalent to:
#        find_package(pybind11 CONFIG REQUIRED)
#   after having potentially altered CMAKE_PREFIX_PATH by adding the path to pybind11 provided
#   by `pip install pybind11`. This is required when using skbuild.
#
#
# litgen_setup_module(bound_library python_native_module_name python_module_name)
# **************************************************************
# litgen_setup_module is a helper function that will
# * link the python native module (.so) to the bound C++ library (bound_library)
# * set the install path of the native module to "." (so that pip install works)
# * copy the native module to bindings/<python_module_name>/<python_native_module_name>.so
#   (so that editable mode works)
# * set the VERSION_INFO macro to the project version defined in CMakeLists.txt
#
#
# **************************************************************
# Note: There are several ways to provide pybind:
#
# - Method 1 (easiest): install pybind11 via pip:
#       pip install pybind11
#
#   This is what happens when building the pip package via skbuild.
#   When building via CMake, you may have to specify PYTHON_EXECUTABLE via
#         -DPYTHON_EXECUTABLE=/path/to/your/venv/bin/python
#
# - Method 2, when using CMake: via a submodule +  add_subdirectory(external/pybind11)
#
option(LITGEN_USE_PIP_PYBIND11 "Use pybind11 provided by ` pip install pyind11 `" ON)


function(_lg_get_python_path out_python_executable)
    if(DEFINED Python3_EXECUTABLE)
        set(${out_python_executable} ${Python3_EXECUTABLE} PARENT_SCOPE)
        return()
    endif()
    if(DEFINED PYTHON_EXECUTABLE)
        set(${out_python_executable} ${PYTHON_EXECUTABLE} PARENT_SCOPE)
        return()
    else()
        find_package(Python3)
        if (Python3_FOUND)
            set(${out_python_executable} ${Python3_EXECUTABLE} PARENT_SCOPE)
        else()
            message(FATAL_ERROR "Python3 not found")
        endif()
    endif()
endfunction()


function(_lg_add_pybind11_pip_cmake_prefix_path)
    _lg_get_python_path(python_executable)

    execute_process(
        COMMAND "${python_executable}" -c
        "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE pybind11_cmake_dir
        OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT
        RESULT_VARIABLE _result
    )
    if(NOT _result EQUAL 0)
        message(FATAL_ERROR "
            Make sure pybind11 is installed via pip:
                pip install pybind11
            Also, make sure you are using the correct python executable:
                -DPYTHON_EXECUTABLE=/path/to/your/venv/bin/python
        ")
    endif()
    set(CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} "${pybind11_cmake_dir}" PARENT_SCOPE)
endfunction()


function(litgen_find_pybind11)
    if(SKBUILD OR LITGEN_USE_PIP_PYBIND11)
        _lg_add_pybind11_pip_cmake_prefix_path()
    endif()
    find_package(pybind11 CONFIG REQUIRED)
endfunction()


function(litgen_setup_module
    # Parameters explanation, with an example: let's say we want to build binding for a C++ library named "foolib",
    bound_library               #  name of the C++ for which we build bindings ("foolib")
    python_native_module_name   #  name of the native python module that provides bindings (for example "_foolib")
    python_module_name          #  name of the standard python module that will import the native module (for example "foolib")
)
    target_link_libraries(${python_native_module_name} PRIVATE ${bound_library})

    # Set python_native_module_name install path to "." (required by skbuild)
    install(TARGETS ${python_native_module_name} DESTINATION ${python_module_name})

    # Copy the python module to the project dir post build (for editable mode)
    set(bindings_module_folder ${PROJECT_SOURCE_DIR}/bindings/${python_module_name})
    set(python_native_module_editable_location ${bindings_module_folder}/$<TARGET_FILE_NAME:${python_native_module_name}>)
    add_custom_target(
        ${python_module_name}_deploy_editable
        ALL
        COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:${python_native_module_name}> ${python_native_module_editable_location}
        DEPENDS ${python_native_module_name}
    )
    target_compile_definitions(${python_native_module_name} PRIVATE VERSION_INFO=${PROJECT_VERSION})
endfunction()