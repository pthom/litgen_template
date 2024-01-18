#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/numpy.h>

#include "imgui.h"
#include "imgui_internal.h"
#include "imgui_docking_internal_types.h"

namespace py = pybind11;



void py_init_module_imgui(py::module& m)
{
    m.def("create_context",
          ImGui::CreateContext,
          py::arg("shared_font_atlas") = py::none(),
          pybind11::return_value_policy::reference);

    auto pyClassImGuiContext =
        py::class_<ImGuiContext>
            (m, "Context", "")
            .def(py::init<ImFontAtlas *>(),
                 py::arg("shared_font_atlas"))
    ;

    auto pyClassImFontAtlas =
        py::class_<ImFontAtlas>
            (m, "ImFontAtlas", "")
            .def(py::init<>())
    ;

}
