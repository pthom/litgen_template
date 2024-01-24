import daft_lib


print("Call any function from the library which you want to debug")
# You can set a breakpoint in the C++ code and debug the call below...
print("For example \n    daft_lib.add(1, 2) = " + str(daft_lib.add(1, 2)))
