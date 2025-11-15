/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 13:27:27 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/25 09:50:42 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*str;
	int		lens;
	int		i;

	i = 0;
	lens = ft_strlen(s);
	str = malloc(lens + 1);
	if (str == NULL)
		return (str);
	while (i < lens)
	{
		str[i] = s[i];
		i++;
	}
	str[i] = '\0';
	return (str);
}
