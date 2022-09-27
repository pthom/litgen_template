#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/numpy.h>

#include "examplelibcpp/examplelibcpp.h"

namespace py = pybind11;


void py_init_module_lg_examplelib(py::module& m)
{
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    // <litgen_pydef> // Autogenerated code below! Do not edit!
    ////////////////////    <generated_from:examplelibcpp.h>    ////////////////////
    m.def("add",
        add, py::arg("a"), py::arg("b"));
    ////////////////////    </generated_from:examplelibcpp.h>    ////////////////////


    ////////////////////    <generated_from:examplelibcpp_2.h>    ////////////////////
    m.def("sub",
        sub, py::arg("a"), py::arg("b"));
    ////////////////////    </generated_from:examplelibcpp_2.h>    ////////////////////

    // </litgen_pydef> // Autogenerated code end
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
}
