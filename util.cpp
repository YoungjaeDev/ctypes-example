#include <string>
#include <iostream>

#define LIBRARY_API extern "C"

LIBRARY_API void print_string(const char* string)
{
    std::cout << string << "\n";
}

LIBRARY_API long long csum(int n, int *array)
{
    long long res = 0;
    for (int i = 0; i < n; ++i)
    {
        res += array[i];
    }
    return res;
}

LIBRARY_API double *add(double *a, double *b)
{
    double *res = new double[3];

    for (int i = 0; i < 3; ++i)
    {
        res[i] = a[i] + b[i];
        //std::cout << a[i] << "\n";
    }

    return res;
}