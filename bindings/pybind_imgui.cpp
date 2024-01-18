#include <pybind11/pybind11.h>

// pybind11/stl.h:
// may be required to take into account ImGuiIO::std::string IniFilename
// (the wheel fails whenever we include it or not)
#include <pybind11/stl.h>


#include "imgui.h"

namespace py = pybind11;

// ImGuiContext is published as an opaque structure.
// We only reproduce its constructor API here.
struct ImGuiContext
{
  // Opaque
  ImGuiContext(ImFontAtlas*);
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
