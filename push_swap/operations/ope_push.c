/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ope_push.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/14 13:48:33 by faribeir          #+#    #+#             */
/*   Updated: 2026/03/14 13:48:36 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void    pa(t_node **stacka, t_node **stackb)
{
    t_node *topb;
    if (!(*stackb))
        return;
    topb = (*stackb)->next;
    (*stackb)->next = (*stacka);
    (*stacka) = (*stackb);
    stackb = topb;
    write(1, "pa\n", 3);
}

void    pb(t_node **stacka, t_node **stackb)
{
    t_node *topa;
    if (!(*stacka))
        return;
    topa = (*stacka)->next;
    (*stacka)->next = (*stackb);
    (*stackb) = (*stacka);
    stacka = topa;
    write(1, "pb\n", 3);
}