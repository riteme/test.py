# test.py
A simple unittest toolchain for C++.

# Usage
## Run tests
By default, `run.py` only recognizes file with suffix `test_` as unittest.  
You can configure it in `conf.py`.  

Most of time, run
```shell
./run.py
```
to run all the unittests.

If you want to run specific tests, run:
```shell
./run.py [filename 1] [filename 2] ...
```

## Write tests
To write a unittest, you should create a unittest file:
```shell
touch test_[testname].cpp
# edit this file.
```

In this file, first include `test.hpp`:
```c++
#include "test.hpp"
```

To begin a unittest, just write like this sample below:
```c++
TESTCASE_GROUP_BEGIN

PREPARE_BEGIN{
    // Preparation.
}PREPARE_END

TESTCASE("Case #1"){
    CHECK(1 + 1 == 2);  // Even 1 + 1 doesn't equal to 2, this won't break this testcase.
    ASSERT(1 + 1 == 3);  // This would break this testcase.
}TESTCASE_END

TESTCASE("Case #2"){
    // Another testcase.
}TESTCASE_END

CLEANUP_BEGIN{
    // Clean-up.
}CLEANUP_END

TESTCASE_GROUP_END

// In the function main():
int main() {
    RUN(true);  // true for details output, false otherwise.

    return 0;
}
```
