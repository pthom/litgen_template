#include <nanobind/nanobind.h>
#include <nanobind/trampoline.h>
#include <nanobind/stl/array.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/vector.h>
#include <nanobind/stl/optional.h>
#include <nanobind/stl/shared_ptr.h>
#include <nanobind/stl/unique_ptr.h>
#include <nanobind/stl/map.h>
#include <nanobind/stl/tuple.h>
#include <nanobind/ndarray.h>

#include "DaftLib/DaftLib.h"

namespace nb = nanobind;

// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// <litgen_glue_code>  // Autogenerated code below! Do not edit!
struct BoxedBool
{
    bool value;
    BoxedBool(bool v = false) : value(v) {}
    std::string __repr__() const { return std::string("BoxedBool(") + std::to_string(value) + ")"; }
};

namespace DaftLib {
// helper type to enable overriding virtual methods in python
class Animal_trampoline : public Animal
{
public:
    NB_TRAMPOLINE(Animal, 1);

    std::string go(int n_times) override
    {
        NB_OVERRIDE_PURE_NAME(
            "go", // function name (python)
            go, // function name (c++)
            n_times // params
        );
    }
};
}  // namespace DaftLib

// </litgen_glue_code> // Autogenerated code end
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


void py_init_module_daft_lib(nb::module_& m)
{
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    // <litgen_pydef> // Autogenerated code below! Do not edit!
    ////////////////////    <generated_from:BoxedTypes>    ////////////////////
    auto pyClassBoxedBool =
        nb::class_<BoxedBool>
            (m, "BoxedBool", "")
        .def_rw("value", &BoxedBool::value, "")
        .def(nb::init<bool>(),
            nb::arg("v") = false)
        .def("__repr__",
            &BoxedBool::__repr__)
        ;
    ////////////////////    </generated_from:BoxedTypes>    ////////////////////


    ////////////////////    <generated_from:DaftLib.h>    ////////////////////
    m.def("add",
        nb::overload_cast<int, int>(DaftLib::add),
        nb::arg("a"), nb::arg("b"),
        "Simple add function (this will be the docstring)");

    m.def("add",
        nb::overload_cast<int, int, int>(DaftLib::add),
        nb::arg("a"), nb::arg("b"), nb::arg("c"),
        "And this is a separate docstring, for this overload");

    m.def("sub",
        DaftLib::sub,
        nb::arg("a"), nb::arg("b"),
        "This is also a docstring,\n on multiple lines");


    auto pyClassPoint =
        nb::class_<DaftLib::Point>
            (m, "Point", " A default constructor with named parameters will\n be automatically generated in python for structs")
        .def("__init__", []( DaftLib::Point *self,
        int x = 0, int y = 0)
        {
            new (self) DaftLib::Point();  // placement new
            auto r = self;
            r->x = x;
            r->y = y;
        },
        nb::arg("x") = 0, nb::arg("y") = 0
        )
        .def_rw("x", &DaftLib::Point::x, "")
        .def_rw("y", &DaftLib::Point::y, "")
        ;


    auto pyClassWidget =
        nb::class_<DaftLib::Widget>
            (m, "Widget", "A class will publish only its public methods and members")
        .def(nb::init<>())
        .def("get_value",
            &DaftLib::Widget::get_value)
        .def("set_value",
            &DaftLib::Widget::set_value, nb::arg("v"))
        ;


    m.def("set_options",
        [](bool v)
        {
            auto SetOptions_adapt_exclude_params = [](bool v)
            {
                DaftLib::SetOptions(v, false);
            };

            SetOptions_adapt_exclude_params(v);
        },
        nb::arg("v"),
        " The parameter priv_param will be excluded from the generated bindings\n since it has a default value, and is excluded via the options.\n See inside tools/autogenerate_bindings.py:\n    options.fn_params_exclude_names__regex = \"^priv_\"");


    auto pyClassAnimal =
        nb::class_<DaftLib::Animal, DaftLib::Animal_trampoline>
            (m, "Animal", " The virtual method of this class can be overriden in python\n see\n    options.class_override_virtual_methods_in_python__regex = \"^Animal$\"")
        .def(nb::init<>()) // implicit default constructor
        .def("go",
            &DaftLib::Animal::go, nb::arg("n_times"))
        ;


    m.def("max_value_int",
        DaftLib::MaxValue<int>,
        nb::arg("values"),
        " MaxValue will be published as max_value_int and max_value_float\n See inside tools/autogenerate_bindings.py:\n    options.fn_template_options.add_specialization(\"^MaxValue$\", [\"int\", \"float\"], add_suffix_to_function_name=True)");
    m.def("max_value_float",
        DaftLib::MaxValue<float>,
        nb::arg("values"),
        " MaxValue will be published as max_value_int and max_value_float\n See inside tools/autogenerate_bindings.py:\n    options.fn_template_options.add_specialization(\"^MaxValue$\", [\"int\", \"float\"], add_suffix_to_function_name=True)");

    m.def("min_value",
        nb::overload_cast<const std::vector<int> &>(DaftLib::MinValue<int>),
        nb::arg("values"),
        " MinValue will be published as min_value for both int and float\n See inside tools/autogenerate_bindings.py:\n    options.fn_template_options.add_specialization(\"^MinValue$\", [\"int\", \"float\"], add_suffix_to_function_name=False)");
    m.def("min_value",
        nb::overload_cast<const std::vector<float> &>(DaftLib::MinValue<float>),
        nb::arg("values"),
        " MinValue will be published as min_value for both int and float\n See inside tools/autogenerate_bindings.py:\n    options.fn_template_options.add_specialization(\"^MinValue$\", [\"int\", \"float\"], add_suffix_to_function_name=False)");

    m.def("get_widget_singleton",
        DaftLib::GetWidgetSingleton,
        " Python should not free the memory of the reference returned by GetWidgetSingleton()\n so we will force the reference policy to be 'reference' instead of 'automatic'\n See\n        options.fn_return_force_policy_reference_for_references__regex = \"Singleton$\"",
        nb::rv_policy::reference);

    m.def("switch_bool_value",
        [](BoxedBool & v)
        {
            auto SwitchBoolValue_adapt_modifiable_immutable = [](BoxedBool & v)
            {
                bool & v_boxed_value = v.value;

                DaftLib::SwitchBoolValue(v_boxed_value);
            };

            SwitchBoolValue_adapt_modifiable_immutable(v);
        },
        nb::arg("v"),
        " SwitchBoolValue is a C++ function that takes a bool parameter by reference and changes its value\n Since bool are immutable in python, we can to use a BoxedBool instead in python.\n See inside tools/autogenerate_bindings.py:\n        options.fn_params_replace_modifiable_immutable_by_boxed__regex = \"^SwitchBoolValue$\"");

    { // <namespace MathFunctions>
        nb::module_ pyNsMathFunctions = m.def_submodule("math_functions", " - This namespace will be published as a python module\n - All functions inside this namespace will be vectorizable\n   (see https://pthom.github.io/litgen/litgen_book/05_05_00_functions.html#vectorize-functions)\n   See inside tools/autogenerate_bindings.py:\n        options.fn_namespace_vectorize__regex = \"^DaftLib::MathFunctions$\"\n        options.fn_vectorize__regex = r\".*\"");
        pyNsMathFunctions.def("log",
            DaftLib::MathFunctions::log, nb::arg("x"));

        pyNsMathFunctions.def("deg_to_rad",
            DaftLib::MathFunctions::deg_to_rad, nb::arg("x"));
    } // </namespace MathFunctions>
    ////////////////////    </generated_from:DaftLib.h>    ////////////////////

    // </litgen_pydef> // Autogenerated code end
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
}
