/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 15:13:20 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/25 09:51:31 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*strcon;
	int		s1len;
	int		s2len;
	int		i;

	i = 0;
	s1len = ft_strlen(s1);
	s2len = ft_strlen(s2);
	strcon = malloc(s1len + s2len + 1);
	if (!strcon)
		return (NULL);
	while (s1[i])
	{
		strcon[i] = s1[i];
		i++;
	}
	i = 0;
	while (s2[i])
	{
		strcon[s1len + i] = s2[i];
		i++;
	}
	strcon[s1len + i] = '\0';
	return (strcon);
}
