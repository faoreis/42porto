/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/14 09:54:02 by faribeir          #+#    #+#             */
/*   Updated: 2026/02/14 10:11:48 by faribeir         ###   ########.fr       */
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

int	ft_validate_arg(int argc, char **list);

#endif
