### Step 2: Customize cpp library name, python package name and pip package name

_(This step is optional if you want to test this template with it default names)_

By default, lg_skbuild_template will use these settings:
* _cpp library name_: a cpp library named "DaftLib" (see `external/DaftLib`) will be built,
  and used as a source to generate python bindings.
* _python package name_: a python package named "daft_lib" will bind this library  
  This python package include a native module named "_daft_lib" which provides the bindings.
* _pip package name_: a pip package named "daft-lib" could be published online

Note: "python package name" can in theory be equal to "pip package name", however there is a gotcha:
*the python package name cannot include "-" (minus), and the pip package name cannot include "_" (underscore)*

> Call `python prepare_template.py` in order to customize this template with your own names.
This is an interactive program that will ask you for those names and prepare this template for you
(it will rename files & directories, and do replacements inside files).
_After this, it is advised to remove prepare_template.py and to commit your folder,
once you made sure that `pip install -v.` works correctly._

__Example session with `python prepare_template.py`__

```
>> python prepare_template.py

* Step 1: enter the name of the cpp library to bind:
a project with this name will be placed inside external/ (you can later replace it with your own)
(in this template, this project is named "DaftLib")

    Name of the cpp library to bind: mylib

Step 2: enter the name of the python package 
Note: this name cannot include "-" (i.e. minus) signs
            
    Name of the python package (enter "d" for default, i.e. lg_mylib): d
    Used lg_mylib as python package name!

Step 3: enter the name of the published pip package. This name can be close to the name of the python package.
Note: this name cannot include "_" (i.e. underscore) sign
        
    Name of the pip package (enter "d" for default, i.e. lg-mylib): d
    Used lg-mylib as pip package name!

Please confirm you want to make the modifications (it cannot be undone). Type 'yes' to confirm: yes
```

_After this, you will see various messages explaining what was changed_

