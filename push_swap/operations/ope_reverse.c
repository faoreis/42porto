/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ope_reverse.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/14 15:17:32 by faribeir          #+#    #+#             */
/*   Updated: 2026/03/14 15:17:37 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	ft_reverse(t_node **stack)
{
    t_node  *last;
    t_node  *first;

    first = *stack;
    while (first->next->next)
        first = first->next;
    last = first->next;
    first->next = NULL;
    last->next = *stack;
    *stack = last;
}

void	rra(t_node **stacka)
{
    if (!(*stacka) || !((*stacka)->next))
        return;
    ft_reverse(stacka);
    write(1, "rra\n", 4);
}

void	rrb(t_node **stackb)
{
    if (!(*stackb) || !((*stackb)->next))
        return;
    ft_reverse(stackb);
    write(1, "rrb\n", 4);
}

void	rrr(t_node **stacka, t_node **stackb)
{
    if ((!(*stacka) || !((*stacka)->next)) || (!(*stackb) || !((*stackb)->next)))
        return;
    ft_reverse(stacka);
    ft_reverse(stackb);
    write(1, "rrr\n", 4);
}
