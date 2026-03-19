/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ope_rotate.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/14 14:07:56 by faribeir          #+#    #+#             */
/*   Updated: 2026/03/19 19:58:31 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	ft_rotate(t_node **stack)
{
	t_node	*first;
	t_node	*last;

	first = (*stack);
	(*stack) = first->next;
	first->next = NULL;
	last = ft_nodelast((*stack));
	last->next = first;
}

void	ra(t_node **stacka)
{
	if (!(*stacka) || !((*stacka)->next))
		return ;
	ft_rotate(stacka);
	write(1, "ra\n", 3);
}

void	rb(t_node **stackb)
{
	if (!(*stackb) || !((*stackb)->next))
		return ;
	ft_rotate(stackb);
	write(1, "rb\n", 3);
}

void	rr(t_node **a, t_node **b)
{
	if ((!(*a) || !((*a)->next)) || (!(*b) || !((*b)->next)))
		return ;
	ft_rotate(a);
	ft_rotate(b);
	write(1, "rr\n", 3);
}
