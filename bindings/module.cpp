#include <pybind11/pybind11.h>


#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)


namespace py = pybind11;


void py_init_module_imgui(py::module& m);


PYBIND11_MODULE(_imgui, m)
{
    py_init_module_imgui(m);
}
