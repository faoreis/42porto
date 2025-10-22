/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 19:26:10 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/17 21:07:47 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	i;
	size_t	j;

	i = 0;
	if (little[0] == '\0')
		return ((char *)big);
	while (i < len && big[i])
	{
		if(big[i] == little[0])
		{
			j = 0;
			while (i +j < len && little[j] && little[j] == big[i + j])
			{
				j++;
			}
			if(little[j] == '\0')
				return ((char *)big + i);
		}
		i++;
	}
	return (NULL);
}
