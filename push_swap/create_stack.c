/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   create_stack.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 20:41:23 by faribeir          #+#    #+#             */
/*   Updated: 2026/03/14 12:10:18 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_node	*ft_add_node(int content, int index)
{
	t_node	*node;

	node = malloc(sizeof(t_node));
	if (!node)
		return (NULL);
	node->num = content;
	node->index = index;
	node->next = NULL;
	return (node);
}

t_node	*ft_insert_stack(char **list, int i)
{
	t_node	*stack;
	t_node	*current;
	t_node	*new;
	int		index;

	stack = NULL;
	current = NULL;
	index = 0;
	while (list[i])
	{
		new = ft_add_node(ft_atoi(list[i]), index++);
		if (!new)
			return (NULL);
		if (!stack)
			stack = new;
		else
			current->next = new;
		current = new;
		i++;
	}
	return (stack);
}

t_node	*ft_create_stack(int argc, char **argv)
{
	int		i;
	char	**list;
	t_node	*stack;

	i = 0;
	if (argc == 2)
		list = ft_split(argv[1], ' ');
	else
	{
		list = argv;
		i = 1;
	}
	stack = ft_insert_stack(list, i);
	if (!stack)
		return (NULL);
	ft_free(list);
	return (stack);
}
