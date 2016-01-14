//
// Copyright 2015 riteme
//

#ifndef NE2D_TEST_HPP_
#define NE2D_TEST_HPP_

#include <vector>
#include <iostream>
#include <functional>

typedef std::function<bool(void)> FunctionType;

struct Testcase {
    Testcase(const std::string &_name, const FunctionType &_func)
            : name(_name), function(_func) {}

    std::string name;
    FunctionType function;
};  // struct Test

static std::vector<Testcase> tests;
static FunctionType prepare = []() -> bool { return true; };
static FunctionType cleanup = []() -> bool { return true; };

void initialize();

#define COLOR_NONE "\033[0m"
#define COLOR_GREEN "\033[34m"
#define COLOR_RED "\033[31m"
#define COLOR_YELLOW "\033[33m"

#define ASSERT(expression)                                    \
    if (!(expression)) {                                      \
        cout << COLOR_RED << "(unittest:fatal)" << COLOR_NONE \
             << " Assert failed: " << #expression << endl;    \
        return false;                                         \
    }

#define CHECK(expression)                                      \
    if (!(expression)) {                                       \
        cout << COLOR_RED << "(unittest:error)" << COLOR_NONE  \
             << " Expression failed: " << #expression << endl; \
        status = false;                                        \
    }

#define DEBUG(msg) \
    cout << COLOR_YELLOW << "(unittest:debug)" << COLOR_NONE << msg << endl;

#define TESTCASE_GROUP_BEGIN void initialize() {
#define TESTCASE_GROUP_END }

#define TESTCASE(name) tests.push_back({ (name), []() -> bool { \
             bool status = true;
#define TESTCASE_END \
    return status;   \
    }                \
    });

#define FATAL return false

#define PREPARE_BEGIN prepare = [&]() -> bool { bool prepare_status = true;
#define PREPARE_END        \
    return prepare_status; \
    }                      \
    ;

#define CLEANUP_BEGIN cleanup = [&]() -> bool { bool cleanup_status = true;
#define CLEANUP_END        \
    return cleanup_status; \
    }                      \
    ;

#define RUN(output)                                                       \
    initialize();                                                         \
    bool flag = true;                                                     \
    if (!prepare()) return -1;                                            \
    for (auto &t : tests) {                                               \
        if ((output))                                                     \
            cout << COLOR_GREEN << "(unittest:info)" << COLOR_NONE << " " \
                 << t.name << endl;                                       \
        flag &= t.function();                                             \
    }                                                                     \
    if (!cleanup()) return -1;                                            \
    if (!flag) return -1;

#endif  // NE2D_TEST_HPP_
