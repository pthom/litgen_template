set(litgen_cmake_help_message "

This Cmake module provides two public functions:


litgen_find_pybind11()
*******************************************************************************
litgen_find_pybind11() will find pybind11 and Python3
It is equivalent to:
    find_package(Python 3.8 REQUIRED COMPONENTS Interpreter Development[.Module])
    find_package(pybind11 CONFIG REQUIRED)
(after having altered CMAKE_PREFIX_PATH by adding the path to pybind11 provided
by `pip install pybind11`. This is helpful when building the C++ library outside of skbuild)

When building via CMake, you may have to specify Python_EXECUTABLE via
     -DPython_EXECUTABLE=/path/to/your/venv/bin/python


litgen_setup_module(bound_library python_native_module_name python_module_name)
*******************************************************************************
litgen_setup_module is a helper function that will:
* link the python native module (.so) to the bound C++ library (bound_library)
* set the install path of the native module to '.' (so that pip install works)
* automatically copy the native module to the python module folder after build
(so that editable mode works even when you modify the C++ library and rebuild)
* set the VERSION_INFO macro to the project version defined in CMakeLists.txt

")

# When building outside of skbuild, we need to add the path to pybind11 provided by pip
function(_lg_add_pybind11_pip_cmake_prefix_path)
    execute_process(
        COMMAND "${Python_EXECUTABLE}" -c
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
                -DPython_EXECUTABLE=/path/to/your/venv/bin/python
        ")
    endif()
    set(CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} "${pybind11_cmake_dir}" PARENT_SCOPE)
endfunction()


function(litgen_find_pybind11)
    if(SKBUILD)
        # we only need the Development.Module component to build native modules
        find_package(Python 3.8 REQUIRED COMPONENTS Interpreter Development.Module)
    else()
        # when building via CMake, we need the full Development component,
        # to be able to debug the native module
        find_package(Python 3.8 REQUIRED COMPONENTS Interpreter Development)
    endif()
    set(Python_EXECUTABLE ${Python_EXECUTABLE} CACHE PATH "Python executable" FORCE)

    if(NOT SKBUILD)
        # when building via CMake, we need to add the path to pybind11 provided by pip
        # (skbuild does it automatically)
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

    # Set VERSION_INFO macro to the project version defined in CMakeLists.txt (absolutely optional)
    target_compile_definitions(${python_native_module_name} PRIVATE VERSION_INFO=${PROJECT_VERSION})

    # Copy the python module to the src/python_bindings post build (for editable mode)
    set(bindings_module_folder ${PROJECT_SOURCE_DIR}/src/python_bindings/${python_module_name})
    set(python_native_module_editable_location ${bindings_module_folder}/$<TARGET_FILE_NAME:${python_native_module_name}>)
    add_custom_target(
        ${python_module_name}_deploy_editable
        ALL
        COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:${python_native_module_name}> ${python_native_module_editable_location}
        DEPENDS ${python_native_module_name}
    )
endfunction()
