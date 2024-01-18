#include <pybind11/pybind11.h>
#include <pybind11/stl.h>


#include "imgui.h"
//#include "imgui_internal.h"
//#include "imgui_docking_internal.h"

namespace py = pybind11;


struct ImGuiContext
{
  // Opaque
  ImGuiContext(ImFontAtlas*) {}
};


void py_init_module_imgui(py::module& m)
{
    m.def("create_context",
          ImGui::CreateContext,
          pybind11::return_value_policy::reference);

    auto pyClassImGuiContext =
        py::class_<ImGuiContext>
            (m, "Context", "")
            .def(py::init<ImFontAtlas *>(),
                 py::arg("shared_font_atlas"))
    ;

    auto pyClassImGuiFontAtlas =
        py::class_<ImFontAtlas>
            (m, "FontAtlas", "")
            .def(py::init<>())
    ;

}
