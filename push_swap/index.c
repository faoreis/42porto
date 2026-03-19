/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   index.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 20:18:58 by faribeir          #+#    #+#             */
/*   Updated: 2026/03/19 20:02:32 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_stack_size(t_node *stack)
{
	int	size;

	size = 0;
	while (stack)
	{
		size++;
		stack = stack->next;
	}
	return (size);
}

int	*ft_fill_array(t_node *stacka, int size)
{
	int	*arr;
	int	i;

	i = 0;
	arr = malloc(size * sizeof(int));
	while (stacka)
	{
		arr[i++] = stacka->num;
		stacka = stacka->next;
	}
	return (arr);
}

void	ft_sort_array(int *arr, int size)
{
	int	i;
	int	j;
	int	tmp;

	i = 0;
	while (i < size -1)
	{
		j = i + 1;
		while (j < size)
		{
			if (arr[i] > arr[j])
			{
				tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
			j++;
		}
		i++;
	}
}

int	ft_get_index(int *arr, int size, int num)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (arr[i] == num)
			return (i);
		i++;
	}
	return (-1);
}

void	ft_index(t_node **stacka)
{
	t_node	*tmp;
	int		*arr;
	int		size;

	size = ft_stack_size(*stacka);
	arr = ft_fill_array(*stacka, size);
	ft_sort_array(arr, size);
	tmp = *stacka;
	while (tmp)
	{
		tmp->index = ft_get_index(arr, size, tmp->num);
		tmp = tmp->next;
	}
	free(arr);
}
