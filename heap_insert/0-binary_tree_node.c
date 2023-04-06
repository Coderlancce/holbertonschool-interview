#include "binary_trees.h"

/**
* binary_tree_node - Creates a binary tree
*
* @parent: node parent
* @value: node with the value
* Return: pointer to nre node or NULL on frailure
*/

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
  binary_tree_t *new;

new = malloc(sizeof(binary_tree_t));
if (new == NULL)
    return (NULL);
    
  new->parent = parent;
  new->n = value;
  new->left = NULL;
  new->right = NULL;
  
  return (new);
}