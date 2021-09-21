#ifndef __SORT__
#define __SORT__

/* imports */
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

/* functions prototypes */
void radix_sort(int *array, size_t size);
int cd_sort(int *array, ssize_t size, int *temp, long exponent);
void print_array(const int *array, size_t size);

#endif
