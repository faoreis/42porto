/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/14 09:54:02 by faribeir          #+#    #+#             */
/*   Updated: 2026/02/18 20:06:53 by faribeir         ###   ########.fr       */
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

#endif
