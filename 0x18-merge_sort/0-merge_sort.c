#include "sort.h"

/**
 * merge - merge function
 * @array: array to be merged
 * @size: size of the array
 * @mid: Middle index
 * @tmp: temp pointer
 * Return: void
 */
void merge(int *array, int size, int mid, int *tmp)
{
	int i, j, k;

	printf("Merging...\n[left]: ");
	print_array(array, mid);
	printf("[right]: ");
	print_array(array + mid, size - mid);
	for (i = 0, j = mid, k = 0; k < size; k++)
	{

		if (j == size)
		{
			tmp[k] = array[i];
			i++;
		}
		else if (i == mid)
		{
			tmp[k] = array[j];
			j++;
		}
		else if (array[j] < array[i])
		{
			tmp[k] = array[j];
			j++;
		}
		else
		{
			tmp[k] = array[i];
			i++;
		}
	}
	for (i = 0; i < size; i++)
	{
		array[i] = tmp[i];
	}
	printf("[Done]: ");
	print_array(tmp, size);
}

/**
 * merge_main - merge function main
 * @array: array to be merged
 * @size: size of the array
 * @tmp: temp pointer
 * Return: void
 */
void merge_main(int *array, size_t size, int *tmp)
{
	int mid;

	if (size < 2)
		return;
	mid = size / 2;
	merge_main(array, mid, tmp);
	merge_main(array + mid,  size - mid, tmp);
	merge(array, size, mid, tmp);
}

/**
 * merge_sort - function to merge sort
 * @array: array to be merged
 * @size: size of the array
 * Return: void
 */
void merge_sort(int *array, size_t size)
{
	int *tmp = NULL;

	if (!array || size < 2)
		return;
	tmp = malloc(sizeof(int) * size);
	if (!tmp)
		return;
	merge_main(array, size, tmp);
	free(tmp);
}