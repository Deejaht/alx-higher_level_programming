#include "hash_tables.h"

/**
 * hash_table_create - function name
 * @size: size of hash table
 *
 * Return: hash_table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *new_table = NULL;

	if (!size)
		return (NULL);
	new_table = malloc(sizeof(hash_node_t *) * size);

	if (!new_table)
		return (NULL);
	return (new_table);
}
