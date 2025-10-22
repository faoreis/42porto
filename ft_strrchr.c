/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 23:15:00 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/16 23:54:47 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char *ft_strrchr(const char *s, int c)
{
	unsigned char	i;
	int	slen;

	i = c;
	slen = ft_strlen(s);
	if (i == '\0')
		return ((char *)(s + slen));
	while (slen >= 0)
	{
		if (s[slen] == i)
			return ((char *)(s + slen));
		slen--;
	}
	return (NULL);
}
