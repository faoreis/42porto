/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/01 12:19:25 by faribeir          #+#    #+#             */
/*   Updated: 2025/11/01 12:28:17 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void*))
{
	t_list	*nnode;

	if (!lst)
		return ;
	while (*lst)
	{
		nnode = (*lst)->next;
		ft_lstdelone(*lst, del);
		*lst = nnode;
	}
}
