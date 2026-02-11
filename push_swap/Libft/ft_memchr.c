/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 09:25:41 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/25 09:47:26 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	const unsigned char	*str;
	unsigned char		b;
	size_t				i;

	i = 0;
	b = c;
	str = s;
	while (i < n)
	{
		if (*str == b)
			return ((char *)str);
		i++;
		str++;
	}
	return (NULL);
}
