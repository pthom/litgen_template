namespace DaftLib
{
    int add(int a, int b);

    // In this example, the parameter v will be "Boxed" into a "BoxedInt"
    // so that modifications can be seen from python
    // See options.fn_params_replace_modifiable_immutable_by_boxed__regex in autogenerate_xxx.py
    inline void inplace_multiply(int * v)
    {
        *v = (*v) * 2;
    }

    inline int sub(int a, int b) { return a - b; }
}
