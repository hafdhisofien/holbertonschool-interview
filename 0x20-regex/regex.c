#include "regex.h"
/**
 * regex_match - matches regex pattern to string
 * @str: the string to scan
 * @pattern: the the regular expression
 * Return: 1 if match else 0
 */
int regex_match(char const *str, char const *pattern)
{
	if (!*str)
		return (!*pattern || (pattern[1] == '*' && regex_match(str, pattern + 2)));
	if (pattern[1] == '*')
		return ((*pattern == '.' || *str == *pattern)
			 ? (regex_match(str + 1, pattern) || regex_match(str, pattern + 2))
			 : (regex_match(str, pattern + 2)));
	return ((*pattern == '.' || *pattern == *str) && regex_match(str + 1, pattern + 1));
}