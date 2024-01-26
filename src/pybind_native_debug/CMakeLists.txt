set(CMAKE_CXX_STANDARD 20)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/dll)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

if(WIN32)
    # set VS_DEBUGGER_ENVIRONMENT to python path defined by PythonEXECUTABLE
    # so that the python dll can be found by the debugger
    # Get parent path of python executable
    get_filename_component(Python_EXECUTABLE_DIR ${Python_EXECUTABLE} DIRECTORY)

    set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT pybind_native_debug)
    set_property(TARGET pybind_native_debug PROPERTY VS_DEBUGGER_ENVIRONMENT "PATH=%PATH%;${Python_EXECUTABLE_DIR}")
endif()

add_executable(pybind_native_debug pybind_native_debug.cpp)
find_package(pybind11 CONFIG REQUIRED)
target_link_libraries(pybind_native_debug PRIVATE pybind11::embed)
