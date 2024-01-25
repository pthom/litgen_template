#include <memory>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>


///////////////////////////////////////////////////////////////////////////////
//  Root namespace
///////////////////////////////////////////////////////////////////////////////
// The namespace DaftLib is the C++ root namespace for the generated bindings
// (i.e. no submodule will be generated for it in the python bindings)
namespace DaftLib
{
    ////////////////////////////////////////////////////////////////////
    // Basic functions bindings
    //////////////////////////////////////////////////////////////////////
    // (Note: this comment will also be published in the python stubs,
    // as a documentation for the users)

    // Simple add function (this will be the docstring)
    int add(int a, int b);

    int add(int a, int b, int c); // And this is a separate docstring, for this overload

    //This is also a docstring,
    // on multiple lines
    inline int sub(int a, int b) { return a - b; }


    ////////////////////////////////////////////////////////////////////
    // Classes and structs bindings
    ////////////////////////////////////////////////////////////////////

    // A default constructor with named parameters will
    // be automatically generated in python for structs
    struct Point
    {
        int x = 0;
        int y = 0;
    };

    // A class will publish only its public methods and members
    class Widget
    {
    public:
        Widget() = default;
        int get_value() const { return m_value; }
        void set_value(int v) { m_value = v; }
    private:
        int m_value = 0;
    };


    ////////////////////////////////////////////////////////////////////
    // Exclude functions and/or parameters from the bindings
    ////////////////////////////////////////////////////////////////////

    // This function will be excluded from the generated bindings
    // See inside tools/autogenerate_bindings.py:
    //    options.fn_exclude_by_name__regex = "^priv_"
    inline void priv_SetOptions(bool v) {}

    // The parameter priv_param will be excluded from the generated bindings
    // since it has a default value, and is excluded via the options.
    // See inside tools/autogenerate_bindings.py:
    //    options.fn_params_exclude_names__regex = "^priv_"
    inline void SetOptions(bool v, bool priv_param = false) {}


    ////////////////////////////////////////////////////////////////////
    // Override virtual methods in python
    ////////////////////////////////////////////////////////////////////

    // The virtual method of this class can be overriden in python
    // see
    //    options.class_override_virtual_methods_in_python__regex = "^Animal$"
    class Animal
    {
    public:
        virtual ~Animal() { }
        virtual std::string go(int n_times) = 0;
    };


    ////////////////////////////////////////////////////////////////////
    // Publish bindings for template functions
    ////////////////////////////////////////////////////////////////////

    // MaxValue will be published as max_value_int and max_value_float
    // See inside tools/autogenerate_bindings.py:
    //    options.fn_template_options.add_specialization("^MaxValue$", ["int", "float"], add_suffix_to_function_name=True)
    template<typename T> T MaxValue(const std::vector<T>& values) { return *std::max_element(values.begin(), values.end());}

    // MinValue will be published as min_value for both int and float
    // See inside tools/autogenerate_bindings.py:
    //    options.fn_template_options.add_specialization("^MinValue$", ["int", "float"], add_suffix_to_function_name=False)
    template<typename T> T MinValue(const std::vector<T>& values) { return *std::min_element(values.begin(), values.end());}


    ////////////////////////////////////////////////////////////////////
    // Return values policy
    ////////////////////////////////////////////////////////////////////

    // Python should not free the memory of the reference returned by GetWidgetSingleton()
    // so we will force the reference policy to be 'reference' instead of 'automatic'
    // See
    //        options.fn_return_force_policy_reference_for_references__regex = "Singleton$"
    inline Widget& GetWidgetSingleton()
    {
        static Widget static_widget;
        return static_widget;
    }


    ////////////////////////////////////////////////////////////////////
    // Boxed types
    ////////////////////////////////////////////////////////////////////

    // SwitchBoolValue is a C++ function that takes a bool parameter by reference and changes its value
    // Since bool are immutable in python, we can to use a BoxedBool instead in python.
    // See inside tools/autogenerate_bindings.py:
    //        options.fn_params_replace_modifiable_immutable_by_boxed__regex = "^SwitchBoolValue$"
    inline void SwitchBoolValue(bool &v) { v = !v; }


    ////////////////////////////////////////////////////////////////////
    // Published vectorized math functions and namespaces
    ////////////////////////////////////////////////////////////////////

    // - This namespace will be published as a python module
    // - All functions inside this namespace will be vectorizable
    //   (see https://pthom.github.io/litgen/litgen_book/05_05_00_functions.html#vectorize-functions)
    //   See inside tools/autogenerate_bindings.py:
    //        options.fn_namespace_vectorize__regex = "^DaftLib::MathFunctions$"
    //        options.fn_vectorize__regex = r".*"
    namespace MathFunctions
    {
        inline double log(double x) { return std::log(x); }
        inline double deg_to_rad(double x) { return x * 3.14159265358979323846 / 180.0; }
    }
}
