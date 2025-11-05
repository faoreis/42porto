/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 19:25:09 by faribeir          #+#    #+#             */
/*   Updated: 2025/11/05 23:18:47 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_al(t_list *nextn, t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	void	*newcontent;

	while (lst)
	{
		newcontent = f(lst -> content);
		if (!newcontent)
			return (0);
		nextn -> next = ft_lstnew(newcontent);
		if (!(nextn -> next))
		{
			del(newcontent);
			return (0);
		}
		nextn = nextn -> next;
		lst = lst -> next;
	}
	return (1);
}

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*newlst;
	t_list	*nextnode;
	void	*newcontent;

	if (!lst)
		return (NULL);
	newcontent = f(lst -> content);
	if (!newcontent)
		return (NULL);
	newlst = ft_lstnew(newcontent);
	if (!newlst)
	{
		del(newcontent);
		return (NULL);
	}
	nextnode = newlst;
	lst = lst -> next;
	if (ft_al(nextnode, lst, f, del))
		return (newlst);
	else
	{
		ft_lstclear(&newlst, del);
		return (NULL);
	}
}
