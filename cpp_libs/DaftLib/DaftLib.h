#include <memory>
#include <string>
#include <cmath>

namespace DaftLib
{
    // Simple add function (this will be the docstring)
    int add(int a, int b);
    inline int sub(int a, int b) { return a - b; } // This is the docstring for `sub`

    // A default constructor with named parameters will
    // be automatically generated in python for structs
    struct Point
    {
        int x;
        int y;

        // The spaceship operator is supported and will generate automatically
        // the correct comparison methods in python
        // (__le__, __lt__, __ge__, __gt__, __eq__, __ne__)
        auto operator<=>(const Point&) const = default;
    };


    // SwitchBoolValue is a C++ function that takes a bool parameter by reference and changes its value
    // Since bool are immutable in python, we can to use a BoxedBool instead in python.
    // See inside tools/autogenerate_bindings.py:
    //        options.fn_params_replace_modifiable_immutable_by_boxed__regex = "^SwitchBoolValue$"
    inline void SwitchBoolValue(bool &v) { v = !v; }

    // This function will be excluded from the generated bindings
    // See inside tools/autogenerate_bindings.py:
    //    options.fn_exclude_by_name__regex = "^priv_"
    inline void priv_SetOptions(bool v) {}

    // The parameter priv_param will be excluded from the generated bindings
    // since it has a default value, and is excluded via the options.
    // See inside tools/autogenerate_bindings.py:
    //    options.fn_params_exclude_names__regex = "^priv_"
    inline void SetOptions(bool v, bool priv_param = false) {}

    class Widget
    {
    public:
        Widget() = default;

        int get_value() const { return m_value; }
        void set_value(int v) { m_value = v; }

    private:
        int m_value = 0;
    };


    // Python should not free the memory of the returned reference,
    // so we will force the reference policy to be 'reference' instead of 'automatic'
    // See
    //        options.fn_return_force_policy_reference_for_references__regex = "Singleton$"
    inline Widget& GetWidgetSingleton()
    {
        static Widget static_widget;
        return static_widget;
    }


    // This namespace will be published as a python module
    // All functions inside this namespace will be vectorizable
    // (see https://pthom.github.io/litgen/litgen_book/05_05_00_functions.html#vectorize-functions)
    // See inside tools/autogenerate_bindings.py:
    //      options.fn_namespace_vectorize__regex = "^MathFunctions$"
    //
    // Marche pas!!!
    namespace MathFunctions
    {
        inline double log(double x) { return std::log(x); }
        inline double deg_to_rad(double x) { return x * 3.14159265358979323846 / 180.0; }
    }

    // The virtual method of this class can be overriden in python
    // see
    //    options.class_override_virtual_methods_in_python__regex = "^Animal$"
    class Animal
    {
    public:
        virtual ~Animal() { }
        virtual std::string go(int n_times) = 0;
    };

    // MaxValue will be published as max_value_int and max_value_float
    // See inside tools/autogenerate_bindings.py:
    //        options.fn_template_options.add_specialization(
    //            "^MaxValue$",
    //            ["int", "float"],
    //            add_suffix_to_function_name=True)
    // template<typename T> T MaxValue(const std::vector<T>& values) { return *std::max_element(values.begin(), values.end());}
}
