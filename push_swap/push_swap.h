/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/14 09:54:02 by faribeir          #+#    #+#             */
/*   Updated: 2026/03/18 22:09:20 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <unistd.h>
# include <stddef.h>
# include <stdlib.h>
# include "Libft/libft.h"

typedef struct s_node
{
	int				num;
	int				index;
	struct s_node	*next;
}	t_node;

void	ft_validate_arg(int argc, char **argv);
int	ft_validade_num(char **num, int i);
int	ft_contains(const char *s1, char **s2, int i);
int	ft_strcmp(const char *s1, const char *s2);
int	ft_isnum(char *num);
void	ft_swap(t_node	**stack);
int	*ft_fill_array(t_node *stacka, int size);
void	ft_sort_array(int *arr, int size);
int	ft_get_index(int *arr, int size, int num);
void	ft_index(t_node **stacka);
void	sa(t_node **a);
void	sb(t_node **b);
void	ss(t_node **a, t_node **b);
void	pa(t_node **stacka, t_node **stackb);
void	pb(t_node **stacka, t_node **stackb);
void	ft_reverse(t_node **stack);
void	rra(t_node **stacka);
void	rrb(t_node **stackb);
void	rrr(t_node **stacka, t_node **stackb);
void	ft_rotate(t_node **stack);
void	ra(t_node **stacka);
void	rb(t_node **stackb);
void	rr(t_node **stacka, t_node **stackb);
t_node	*ft_add_node(int content, int index);
t_node	*ft_insert_stack(char **list, int i);
t_node	*ft_create_stack(int argc, char **argv);
void	ft_free(char **list);
//int	ft_stack_size(t_node *stack);
t_node	*ft_nodelast(t_node *lst);
void sort_5(t_node **stacka, t_node **stackb);
void	sort_3(t_node **stack);
int get_chunk_size(int size);
void push_chunks(t_node **a, t_node **b);
int find_max_pos(t_node *b);
void push_back(t_node **a, t_node **b);
void sort_big(t_node **a, t_node **b);
int	stack_size(t_node *stack);


#endif
