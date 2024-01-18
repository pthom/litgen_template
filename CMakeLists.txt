cmake_minimum_required(VERSION 3.17)
project(lg_template VERSION "0.0.1")


set(CMAKE_CXX_STANDARD 20)


####################################################
# Add pybind11
####################################################
# Note there are several ways to provide pybind:
# - Method 1 (easiest): `pip install pybind11`
#       This is the default in this template (when LITGEN_USE_PIP_PYBIND11 is ON which is the default)
#       You may have to specify PYTHON_EXECUTABLE via -DPYTHON_EXECUTABLE=/path/to/your/venv/bin/python
# - Method 2: via a submodule +  add_subdirectory(external/pybind11)

option(LITGEN_USE_PIP_PYBIND11 "Use pybind11 provided by ` pip install pyind11 `" ON)

# if pybind11 is installed via pip, then add its path to CMAKE_PREFIX_PATH
function(_lg_add_pybind11_pip_cmake_prefix_path)
    if(NOT DEFINED PYTHON_EXECUTABLE)
        find_package(Python3)
        if (NOT Python3_FOUND)
            message(FATAL_ERROR "Python3 not found")
        endif()
        set(PYTHON_EXECUTABLE ${Python3_EXECUTABLE})
    endif()
    execute_process(
        COMMAND "${PYTHON_EXECUTABLE}" -c
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


if(SKBUILD OR LITGEN_USE_PIP_PYBIND11)
    _lg_add_pybind11_pip_cmake_prefix_path()
endif()
find_package(pybind11 CONFIG REQUIRED)


####################################################
# Build examplelibcpp Bound C++ library
####################################################
set(imgui_dir external/imgui)
add_subdirectory(${imgui_dir})


#########################################################################
# Build python module that provides bindings to the library implot
#########################################################################
include(litgen_cmake/litgen_setup_module.cmake)

set(bound_library imgui)          # The library for which we are building bindings
set(python_native_module_name _imgui) # This is the native python module name
set(python_wrapper_module_name imgui) # This is the python wrapper around the native module
set(python_module_sources bindings/module.cpp bindings/pybind_${bound_library}.cpp) # native python module sources

pybind11_add_module(${python_native_module_name} ${python_module_sources})
target_compile_definitions(_imgui PRIVATE VERSION_INFO=${PROJECT_VERSION})
litgen_setup_module(
    ${bound_library}
    ${python_native_module_name}
    ${python_wrapper_module_name}
)
