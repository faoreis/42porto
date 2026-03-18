/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ckunk.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 23:19:27 by faribeir          #+#    #+#             */
/*   Updated: 2026/03/18 23:22:28 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int get_chunk_size(int size)
{
    if (size <= 100)
        return 15;
    return 30;
}

void push_chunks(t_node **a, t_node **b)
{
    int i = 0;
    int size = stack_size(*a);
    int chunk = get_chunk_size(size);

    while (*a)
    {
        if ((*a)->index <= i)
        {
            pb(a, b);
            rb(b);
            i++;
        }
        else if ((*a)->index <= i + chunk)
        {
            pb(a, b);
            i++;
        }
        else
            ra(a);
    }
}

int find_max_pos(t_node *b)
{
    int max = b->index;
    int pos = 0;
    int i = 0;

    while (b)
    {
        if (b->index > max)
        {
            max = b->index;
            pos = i;
        }
        b = b->next;
        i++;
    }
    return pos;
}

void push_back(t_node **a, t_node **b)
{
    int pos;
    int size;

    while (*b)
    {
        pos = find_max_pos(*b);
        size = stack_size(*b);

        if (pos <= size / 2)
        {
            while (pos--)
                rb(b);
        }
        else
        {
            pos = size - pos;
            while (pos--)
                rrb(b);
        }
        pa(a, b);
    }
}

void sort_big(t_node **stacka, t_node **stackb)
{
    push_chunks(stacka, stackb);
    push_back(stacka, stackb);
}
