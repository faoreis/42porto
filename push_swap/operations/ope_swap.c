/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ope_swap.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/14 12:56:45 by faribeir          #+#    #+#             */
/*   Updated: 2026/03/19 19:54:30 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	ft_swap(t_node	**stack)
{
	t_node	*temp;

	temp = (*stack);
	(*stack) = (*stack)->next;
	temp->next = (*stack)->next;
	(*stack)->next = temp;
}

void	sa(t_node **a)
{
	if (!(*a) || !((*a)->next))
		return ;
	ft_swap(a);
	write(1, "sa\n", 3);
}

void	sb(t_node **b)
{
	if (!(*b) || !((*b)->next))
		return ;
	ft_swap(b);
	write(1, "sb\n", 3);
}

void	ss(t_node **a, t_node **b)
{
	if ((!(*b) || !((*b)->next)) || (!(*a) || !((*a)->next)))
		return ;
	ft_swap(a);
	ft_swap(b);
	write(1, "ss\n", 3);
}
