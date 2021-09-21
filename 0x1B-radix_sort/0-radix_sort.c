#include "sort.h"

/**
 * radix_sort - function to perform radix sort
 * @array: array to sort
 *
 * @size: size of the array
 */
void radix_sort(int *array, size_t size)
{
	size_t i;
	long exponent = 1;
	int *temp, min_int = INT_MIN;

	if (size < 2 || !array)
		return;

	temp = malloc(sizeof(int *) * size);
	if (!temp)
		return;

	for (i = 0; i < size; i++)
		min_int = array[i] > min_int ? array[i] : min_int;

	while (min_int / exponent > 0)
	{
		cd_sort(array, size, temp, exponent);
		print_array(array, size);
		exponent *= 10;
	}
	free(temp);
}

/**
 * cd_sort - current digit sort
 * @array: array to sort
 * @size: size of the array
 * @temp: temporal array
 * @exponent: exponent number
 *
 * Return: array sort
 */
int cd_sort(int *array, ssize_t size, int *temp, long exponent)
{
	ssize_t i;
	int aux[10] = {0};

	for (i = 0; i < size; i++)
		aux[(array[i] / exponent) % 10]++, temp[i] = 0;

	for (i = 1; i < 10; i++)
		aux[i] += aux[i - 1];

	for (i = size - 1; i >= 0; i--)
		temp[--aux[(array[i] / exponent) % 10]] = array[i];

	for (i = 0; i < size; i++)
		array[i] = temp[i];

	return (0);
}
