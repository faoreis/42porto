/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/10 21:13:21 by faribeir          #+#    #+#             */
/*   Updated: 2026/03/19 22:35:28 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_contains(const char *s1, char **s2, int i)
{
	int	compar;

	compar = 1;
	i++;
	while (s2[i] && compar != 0)
	{
		compar = ft_strcmp(s1, s2[i]);
		i++;
	}
	if (compar == 0)
		return (1);
	else
		return (0);
}

int	ft_isnum(char *num)
{
	int	i;
	int	nnum;

	nnum = 0;
	i = 0;
	if (num[i] == '-' || num[i] == '+')
		i++;
	while (num[i] && !nnum)
	{
		if (num[i] < '0' || num[i] > '9')
			nnum = 1;
		i++;
	}
	return (nnum);
}

int	ft_validade_num(char **num, int i)
{
	int	lerror;
	long	tempnum;

	lerror = 0;
	while (num[i] && !lerror)
	{
		lerror = ft_isnum(num[i]);
		if (!lerror)
			lerror = ft_contains(num[i], num, i);
		if (!lerror)
		{
			tempnum = ft_atoi(num[i]);
			if (tempnum < -2147483648 || tempnum > 2147483647)
				lerror = 1;
		}
		i++;
	}
	return (lerror);
}

void	ft_validate_arg(int argc, char **argv)
{
	int			i;
	int			lerror;
	char		**list;

	i = 0;
	if (argc == 2)
		list = ft_split(argv[1], ' ');
	else
	{
		list = argv;
		i = 1;
	}	
	lerror = ft_validade_num(list, i);
	if (lerror)
	{
		if (argc == 2)
			ft_free(list);
		write(1, "Error\n", 6);
		exit(0);
	}
	if (argc == 2)
		ft_free(list);
}

#include <stdio.h>
int	main(int argc, char **argv)
{
	t_node	*stacka;
	t_node	*stackb;

	if (argc == 1)
		return (0);
	ft_validate_arg(argc, argv);
	stacka = ft_create_stack(argc, argv);
	stackb = NULL;
	if (!stacka)
		return (write(1, "Error\n", 6));	
	ft_index(&stacka);
	if (stack_size(stacka) == 2)
		sa(&stacka);
	else if (stack_size(stacka) == 3)
		sort_3(&stacka);
	else if (stack_size(stacka) <= 5)
		sort_5(&stacka, &stackb);
	else
		sort_big(&stacka, &stackb);
	t_node *tmp;
	tmp = stacka;	
	while (tmp)
	{
		printf("num: [%d]\n", tmp->num);
		printf("index: [%d]\n", tmp->index);
		tmp = tmp->next;
	}
	ft_free_stack(stacka);
	return (0);
}

