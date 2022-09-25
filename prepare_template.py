from __future__ import annotations
import os
from dataclasses import dataclass


_THIS_DIR = os.path.dirname(os.path.realpath(__file__))


@dataclass
class PackageNames:
    """
    By default, lg_skbuild_template will use the following names:
        * The library for which we build bindings is "example_lib_cpp"
        * The name of the python package that binds this library is "example_lib" (this name cannot include "-").
          This python package include a native module named "_example_lib" which provides the bindings.
        * The name of the pip package is "example-lib" (this name cannot include "_")
          (the pip package name can be slightly different from the python package name)
    """
    cpp_library_name = "example_lib_cpp"
    python_package_name = "example_lib"
    pip_package_name = "example-lib"

    @staticmethod
    def _template_default_package_names():
        r = PackageNames()
        return r
    
    def replace_in_string(self, s: str) -> str:
        default_names = PackageNames._template_default_package_names()
        r = s
        r = r.replace(default_names.cpp_library_name, self.cpp_library_name)
        r = r.replace(default_names.python_package_name, self.python_package_name)
        r= r.replace(default_names.pip_package_name, self.pip_package_name)
        return r

    def replace_in_file(self, filename: str):
        valid_extensions = ["py", "cpp", "h", "pyi", "txt", "toml", "ini", "yaml", "md", "yml"]
        ok = False
        for extension in valid_extensions:
            if filename.endswith(extension):
                ok = True
        if not ok:
            print(f"skipping {filename}")
            return

        print(f"_replace_in_file {filename}")

        with open(filename, "r") as input_file:
            content = input_file.read()
            content = self.replace_in_string(content)

        with open(filename, "w") as outputfile:
            outputfile.write(content)

    def replace_in_files(self) -> None:
        default_names = PackageNames._template_default_package_names()
        # Directories where to replace by the new names:
        directories = [
            ".github/workflows",
            "./bindings",
            f"./bindings/{default_names.python_package_name}",
            f"./external/{default_names.cpp_library_name}",
            "./conda.recipe",
            "./tests",
            ".",
        ]

        for directory in directories:
            files = os.listdir(f"{directory}")
            for file in files:
                file_fullpath = f"{directory}/{file}"
                if os.path.isfile(file_fullpath) and file != "prepare_template.py":
                    self.replace_in_file(file_fullpath)

    def rename_files(self) -> None:
        """
        Directories and files to rename:
            ./bindings/example_lib
            ./external/example_lib_cpp
            ./external/example_lib_cpp/example_lib_cpp.h
            ./external/example_lib_cpp/example_lib_cpp.cpp
            ./external/example_lib_cpp/example_lib_cpp_2.h
            ./external/example_lib_cpp/example_lib_cpp_2.cpp
            ./tests/example_lib_test.py
            autogenerate_example_lib.py
        """
        default_names = PackageNames._template_default_package_names()
        dir_and_files_to_rename = [
            f"./bindings/{default_names.python_package_name}/",
            f"./bindings/pybind_{default_names.cpp_library_name}.cpp",

            f"./external/{default_names.cpp_library_name}/",

            f"autogenerate_{default_names.python_package_name}.py",
            f"{default_names.cpp_library_name}_amalgamation.h",

            f"tests/{default_names.python_package_name}_test.py"
        ]

        for pathname in dir_and_files_to_rename:
            new_pathname = self.replace_in_string(pathname)
            src = f"{pathname}"
            dst = f"{new_pathname}"
            print(f"os.rename({src}, {dst})")
            os.rename(src, dst)

        default_names = PackageNames()
        os.rename(
            f"external/{self.cpp_library_name}/{default_names.cpp_library_name}.h",
            f"external/{self.cpp_library_name}/{self.cpp_library_name}.h")
        os.rename(
            f"external/{self.cpp_library_name}/{default_names.cpp_library_name}.cpp",
            f"external/{self.cpp_library_name}/{self.cpp_library_name}.cpp")
        os.rename(
            f"external/{self.cpp_library_name}/{default_names.cpp_library_name}_2.h",
            f"external/{self.cpp_library_name}/{self.cpp_library_name}_2.h")
        os.rename(
            f"external/{self.cpp_library_name}/{default_names.cpp_library_name}_2.cpp",
            f"external/{self.cpp_library_name}/{self.cpp_library_name}_2.cpp")

    def do_replace(self) -> None:
        self.replace_in_files()
        self.rename_files()

    @staticmethod
    def help():
        help_prepare = PackageNames.__doc__ + """

        This utility will make the modifications in order to use new names (replace in files, rename files & folders).
        """
        print(help_prepare)

    @staticmethod
    def from_user_input() -> PackageNames:
        r = PackageNames()

        # Step 1: ask for cpp library name
        print("""
* Step 1: enter the name of the cpp library to bind: 
a project with this name will be placed inside external/ (you can later replace it with your own)
(in this template, this project is named "examplelib")
            """)
        r.cpp_library_name = input(f"    Name of the cpp library to bind: ")

        # Step 2: ask for python package name
        default_python_package_name = "lg_" + r.cpp_library_name
        print(f"""
Step 2: enter the name of the python package 
If you enter "d" or nothing, the default name will be used, i.e.           "{default_python_package_name}"
Note: this name cannot include "-" (i.e. minus) signs
        """)
        r.python_package_name = input('    Name of the python package: ')
        if r.python_package_name.lower() == "d" or r.python_package_name == "":
            r.python_package_name = default_python_package_name
            print(f"    Used {default_python_package_name} as python package name!")

        # Step 3: ask for pip package name
        default_pip_package_name = r.python_package_name.replace("_", "-")
        print(f"""
Step 3: enter the name of the published pip package. This name can be close to the name of the python package.
If you enter "d" or nothing, the default name will be used, i.e.            "{default_pip_package_name}"
Note: this name cannot include "_" (i.e. underscore) sign
        """)
        r.pip_package_name = input(
            f'    Name of the pip package: ')
        if r.pip_package_name.lower() == "d" or r.pip_package_name == "":
            r.pip_package_name = default_pip_package_name
            print(f"    Used {default_pip_package_name} as pip package name!")

        return r


def main():
    os.chdir(_THIS_DIR)
    interactive = True
    if interactive:
        PackageNames.help()

        package_names = PackageNames.from_user_input()
        answer = input(
            "Please confirm you want to make the modifications (it cannot be undone). Type 'yes' to confirm: ")
        if answer != "yes":
            print("Cancelled!")
            return
    else:
        package_names = PackageNames()
        package_names.cpp_library_name = "..."
        package_names.python_package_name = "..."
        package_names.pip_package_name = "..."
        raise NotImplementedError("Please fill in the names in the code")

    package_names.do_replace()


if __name__ == "__main__":
    main()

