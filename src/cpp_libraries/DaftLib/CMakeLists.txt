add_library(DaftLib STATIC cpp/DaftLib.cpp DaftLib.h)
target_include_directories(DaftLib PUBLIC ${CMAKE_CURRENT_LIST_DIR}/..)

# Under windows, auto __declspec(dllexport)
if (WIN32)
    set_target_properties(DaftLib PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()
