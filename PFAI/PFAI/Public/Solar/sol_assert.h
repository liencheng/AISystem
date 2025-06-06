#pragma once
#include <stdexcept>
#include <iostream>
#include <stdexcept>
#include <string>
#include <iostream>

#define __SOL_TRACE		{}
#define SOL_TRACE__		{}



// ��̬���Ժ������׳��쳣��
inline void dynamicAssert(bool condition, const char* exprStr, const char* msg, const char* file, int line) {
    if (!condition) {
        std::string error = "Assertion failed: (";
        error += exprStr;
        error += ") ";
        error += msg;
        error += " at ";
        error += file;
        error += ":";
        error += std::to_string(line);
        throw std::runtime_error(error);
    }
}

// ��ȫ�Ķ��Ժ�
#define SOL_ASSERT(expr, msg) \
    do { \
        dynamicAssert((expr), #expr, msg, __FILE__, __LINE__); \
    } while (false)

