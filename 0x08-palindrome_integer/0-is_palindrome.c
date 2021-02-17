#include "palindrome.h"

/**
 * is_palindrome - checks whether or not a given unsigned integer is a palindrome
 * @n: is the number to be checked
 *
 * Return: 1 if n is a palindrome, and 0 otherwise
 */
int is_palindrome(unsigned long n)
{
	int ret, total = 0, temp;

	temp = n;
	while (n > 0)
	{
		ret = n % 10;
		total = (total * 10) + ret;
		n /= 10;
	}
	if (temp == total)
		return (1);
	else
		return (0);
}