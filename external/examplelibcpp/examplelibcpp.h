#include <string>
#include <memory>

namespace examplelib
{
    struct Foo
    {
        int a = 1;
        std::string s;
    };

    Foo* MakeFoo()
    {
        // Yes, it leaks. It's a test.
        Foo* r = new Foo();
        r->s = "hello";
        return r;
    }

}
