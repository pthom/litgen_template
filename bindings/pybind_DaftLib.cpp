#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/numpy.h>

#include "DaftLib/DaftLib.h"

namespace py = pybind11;


// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// <litgen_glue_code>  // Autogenerated code below! Do not edit!
struct BoxedInt
{
    int value;
    BoxedInt(int v = 0) : value(v) {}
    std::string __repr__() const { return std::string("BoxedInt(") + std::to_string(value) + ")"; }
};

// </litgen_glue_code> // Autogenerated code end
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



void py_init_module_daft_lib(py::module& m)
{
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    // <litgen_pydef> // Autogenerated code below! Do not edit!
    ////////////////////    <generated_from:BoxedTypes>    ////////////////////
    auto pyClassBoxedInt =
        py::class_<BoxedInt>
            (m, "BoxedInt", "")
        .def_readwrite("value", &BoxedInt::value, "")
        .def(py::init<int>(),
            py::arg("v") = 0)
        .def("__repr__",
            &BoxedInt::__repr__)
        ;
    ////////////////////    </generated_from:BoxedTypes>    ////////////////////


    ////////////////////    <generated_from:DaftLib.h>    ////////////////////
    m.def("add",
        DaftLib::add, py::arg("a"), py::arg("b"));

    m.def("inplace_multiply",
        [](BoxedInt & v)
        {
            auto inplace_multiply_adapt_modifiable_immutable = [](BoxedInt & v)
            {
                int * v_boxed_value = & (v.value);

                DaftLib::inplace_multiply(v_boxed_value);
            };

            inplace_multiply_adapt_modifiable_immutable(v);
        },
        py::arg("v"),
        " In this example, the parameter v will be \"Boxed\" into a \"BoxedInt\"\n so that modifications can be seen from python\n See options.fn_params_replace_modifiable_immutable_by_boxed__regex in autogenerate_xxx.py");

    m.def("sub",
        DaftLib::sub, py::arg("a"), py::arg("b"));
    ////////////////////    </generated_from:DaftLib.h>    ////////////////////

    // </litgen_pydef> // Autogenerated code end
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
}
