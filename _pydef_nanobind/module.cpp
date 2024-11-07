#include <nanobind/nanobind.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)


namespace nb = nanobind;


void py_init_module_daft_lib(nb::module_& m);


// This builds the native python module `_daft_lib`
// it will be wrapped in a standard python module `daft_lib`
NB_MODULE(_daft_lib, m)
{
    #ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
    #else
    m.attr("__version__") = "dev";
    #endif

    py_init_module_daft_lib(m);
}
