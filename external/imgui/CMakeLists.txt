add_library(imgui STATIC imgui.cpp imgui_draw.cpp imgui_widgets.cpp imgui_demo.cpp imgui_tables.cpp)
target_include_directories(imgui PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_compile_options(imgui PUBLIC -fPIC)
target_compile_definitions(imgui PUBLIC IMGUI_WITH_STRING)
