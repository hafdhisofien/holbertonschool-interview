#include "binary_trees.h"
/**
    *binary_tree_node - creates binary tree
    *@parent: is a pointer to the parent node of the node to create
    *@value: is the value to put in the new node
    *When created, a node does not have any children
    *Return: pointer to the new node, or NULL on failure
 */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new;

	new = malloc(sizeof(binary_tree_t));
	if (!new)
		return (NULL);
	new->parent = parent;
	new->n = value;
	new->left = NULL;
	new->right = NULL;

	return (new);
}
