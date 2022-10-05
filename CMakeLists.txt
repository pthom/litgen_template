cmake_minimum_required(VERSION 3.17)
project(lg_template VERSION "0.0.1")

include(lg_cmake_utils/lg_cmake_utils.cmake)

set(CMAKE_CXX_STANDARD 20)

####################################################
# Add pybind11
####################################################
if(DEFINED PYTHON_EXECUTABLE)
    # Find pybind11 when building the pip module
    # pybind is referenced in pyproject.toml, section [build-system]/requires

    # Scikit-Build does not add your site-packages to the search path
    # automatically, so we need to add it _or_ the pybind11 specific directory
    # here.
    execute_process(
        COMMAND "${PYTHON_EXECUTABLE}" -c
        "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE _tmp_dir
        OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
    list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")

    # Now we can find pybind11
    find_package(pybind11 CONFIG REQUIRED)
else()
    # Find pybind11 in a standard build (not driven by pip)

    # Method 1: via a submodule
    # add_subdirectory(external/pybind11)

    # Method 2: via a global install + find_package (e.g `brew install pybind11`, `apt-get install python-pybind11`)
    find_package(pybind11 CONFIG REQUIRED)
endif()


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
