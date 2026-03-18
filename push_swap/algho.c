/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algho.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/17 19:50:36 by faribeir          #+#    #+#             */
/*   Updated: 2026/03/17 19:50:39 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int stack_size(t_node *stack)
{
    int size = 0;

    while (stack)
    {
        size++;
        stack = stack->next;
    }
    return size;
}

int find_min_pos(t_node *stack)
{
    int min = stack->index;
    int pos = 0;
    int i = 0;

    while (stack)
    {
        if (stack->index < min)
        {
            min = stack->index;
            pos = i;
        }
        stack = stack->next;
        i++;
    }
    return pos;
}

void move_min_to_top(t_node **stack)
{
    int pos;
    int size;

    pos = find_min_pos(*stack);
    size = stack_size(*stack);

    if (pos <= size / 2)
    {
        while (pos--)
            ra(stack);
    }
    else
    {
        pos = size - pos;
        while (pos--)
            rra(stack);
    }
}

void sort_3(t_node **stack)
{
    int a;
    int b;
    int c;

    a = (*stack)->index;
    b = (*stack)->next->index;
    c = (*stack)->next->next->index;

    if (a > b && b < c && a < c)
        sa(stack);
    else if (a > b && b > c)
    {
        sa(stack);
        rra(stack);
    }
    else if (a > b && b < c && a > c)
        ra(stack);
    else if (a < b && b > c && a < c)
    {
        sa(stack);
        ra(stack);
    }
    else if (a < b && b > c && a > c)
        rra(stack);
}

void sort_5(t_node **stacka, t_node **stackb)
{
    while (stack_size(*stacka) > 3)
    {
        move_min_to_top(stacka);
        pb(stacka, stackb);
    }
    sort_3(stacka);
    while (*stackb)
        pa(stacka, stackb);
}