# If you want to use mypy or pyright, you may have to ignore some errors, like below:

# mypy: disable-error-code="override"
# pyright: reportIncompatibleMethodOverride=false

from typing import overload
import numpy as np

NumberType = (int, float, np.number)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:BoxedTypes>    ####################
class BoxedBool:
    value: bool
    def __init__(self, v: bool = False) -> None:
        pass
    def __repr__(self) -> str:
        pass

####################    </generated_from:BoxedTypes>    ####################

####################    <generated_from:DaftLib.h>    ####################

# //////////////////////////////////////////////////////////////////
# Basic functions bindings
# (Note: this comment will also be published in the python stubs,
# as a documentation for the users)
# //////////////////////////////////////////////////////////////////

@overload
def add(a: int, b: int) -> int:
    """Simple add function (this will be the docstring)"""
    pass

@overload
def add(a: int, b: int, c: int) -> int:
    """And this is a separate docstring, for this overload"""
    pass

def sub(a: int, b: int) -> int:
    """This is also a docstring,
    on multiple lines
    """
    pass

# //////////////////////////////////////////////////////////////////
# Classes and structs bindings
# ////////////////////////////////////////////////////////////////

class Point:
    """A default constructor with named parameters will
    be automatically generated in python for structs
    """

    x: int
    y: int

    def __lt__(self, param_0: Point) -> bool:
        """The spaceship operator is supported and will generate automatically
         the correct comparison methods in python
         (__le__, __lt__, __ge__, __gt__, __eq__, __ne__)


        (C++ auto return type)
        """
        pass
    def __le__(self, param_0: Point) -> bool:
        """The spaceship operator is supported and will generate automatically
         the correct comparison methods in python
         (__le__, __lt__, __ge__, __gt__, __eq__, __ne__)


        (C++ auto return type)
        """
        pass
    def __eq__(self, param_0: Point) -> bool:
        """The spaceship operator is supported and will generate automatically
         the correct comparison methods in python
         (__le__, __lt__, __ge__, __gt__, __eq__, __ne__)


        (C++ auto return type)
        """
        pass
    def __ge__(self, param_0: Point) -> bool:
        """The spaceship operator is supported and will generate automatically
         the correct comparison methods in python
         (__le__, __lt__, __ge__, __gt__, __eq__, __ne__)


        (C++ auto return type)
        """
        pass
    def __gt__(self, param_0: Point) -> bool:
        """The spaceship operator is supported and will generate automatically
         the correct comparison methods in python
         (__le__, __lt__, __ge__, __gt__, __eq__, __ne__)


        (C++ auto return type)
        """
        pass
    def __init__(self, x: int = int(), y: int = int()) -> None:
        """Auto-generated default constructor with named params"""
        pass

class Widget:
    """A class will publish only its public methods and members"""

    def __init__(self) -> None:
        pass
    def get_value(self) -> int:
        pass
    def set_value(self, v: int) -> None:
        pass

def get_widget_singleton() -> Widget:
    """Python should not free the memory of the returned reference,
    so we will force the reference policy to be 'reference' instead of 'automatic'
    See
           options.fn_return_force_policy_reference_for_references__regex = "Singleton$"
    """
    pass

def switch_bool_value(v: BoxedBool) -> None:
    """SwitchBoolValue is a C++ function that takes a bool parameter by reference and changes its value
    Since bool are immutable in python, we can to use a BoxedBool instead in python.
    See inside tools/autogenerate_bindings.py:
           options.fn_params_replace_modifiable_immutable_by_boxed__regex = "^SwitchBoolValue$"
    """
    pass

def set_options(v: bool) -> None:
    """The parameter priv_param will be excluded from the generated bindings
    since it has a default value, and is excluded via the options.
    See inside tools/autogenerate_bindings.py:
       options.fn_params_exclude_names__regex = "^priv_"
    """
    pass

class Animal:
    """The virtual method of this class can be overriden in python
    see
       options.class_override_virtual_methods_in_python__regex = "^Animal$"
    """

    def go(self, n_times: int) -> str:  # overridable (pure virtual)
        pass
    def __init__(self) -> None:
        """Autogenerated default constructor"""
        pass

# MaxValue will be published as max_value_int and max_value_float
# See inside tools/autogenerate_bindings.py:
#        options.fn_template_options.add_specialization(
#            "^MaxValue$",
#            ["int", "float"],
#            add_suffix_to_function_name=True)
# template<typename T> T MaxValue(const std::vector<T>& values) { return *std::max_element(values.begin(), values.end());}

# <submodule math_functions>
class math_functions:  # Proxy class that introduces typings for the *submodule* math_functions
    pass  # (This corresponds to a C++ namespace. All method are static!)
    """ This namespace will be published as a python module
     All functions inside this namespace will be vectorizable
     (see https://pthom.github.io/litgen/litgen_book/05_05_00_functions.html#vectorize-functions)
     See inside tools/autogenerate_bindings.py:
          options.fn_namespace_vectorize__regex = "^MathFunctions$"

     Marche pas!!!
    """
    @staticmethod
    def log(x: float) -> float:
        pass
    @staticmethod
    def deg_to_rad(x: float) -> float:
        pass

# </submodule math_functions>
####################    </generated_from:DaftLib.h>    ####################

# </litgen_stub>
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
