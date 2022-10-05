cmake_minimum_required(VERSION 3.17)
project(lg_template VERSION "0.0.1")

include(lg_cmake_utils/lg_cmake_utils.cmake)

set(CMAKE_CXX_STANDARD 20)

####################################################
# Add pybind11
####################################################
# Note there are several ways to provide pybind:
# - Method 1 (easiest): `pip install pybind11` and specify PYTHON_EXECUTABLE
# - Method 2: via a submodule +  add_subdirectory(external/pybind11)
# - Method 3: via a global install (`brew install pybind11`, `apt-get install python-pybind11`)
#      Note that apt packages may be out of date and might break the build (we require pybind11 from late 2021)
if(DEFINED PYTHON_EXECUTABLE)
    # if PYTHON_EXECUTABLE is defined, and pybind11 is installed via pip,
    # then add its path to CMAKE_PREFIX_PATH
    #
    # this is the case
    # * when using SKBUILD, which set PYTHON_EXECUTABLE
    #   (and pybind11 is referenced in pyproject.toml, section [build-system]/requires)
    # * when building normally, if you set PYTHON_EXECUTABLE
    execute_process(
        COMMAND "${PYTHON_EXECUTABLE}" -c
        "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE _tmp_dir
        OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
    list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")
endif()

find_package(pybind11 CONFIG REQUIRED)


####################################################
# Build examplelibcpp Bound C++ library
####################################################
set(examplelibcpp_dir external/examplelibcpp)
add_subdirectory(${examplelibcpp_dir})


#########################################################################
# Build python module that provides bindings to the library implot
#########################################################################
set(bound_library examplelibcpp)          # The library for which we are building bindings
set(python_native_module_name _lg_examplelib) # This is the native python module name
set(python_wrapper_module_name lg_examplelib) # This is the python wrapper around the native module
set(python_module_sources bindings/module.cpp bindings/pybind_${bound_library}.cpp) # native python module sources

pybind11_add_module(${python_native_module_name} ${python_module_sources})
target_compile_definitions(_lg_examplelib PRIVATE VERSION_INFO=${PROJECT_VERSION})
lg_setup_module(
    ${bound_library}
    ${python_native_module_name}
    ${python_wrapper_module_name}
)
