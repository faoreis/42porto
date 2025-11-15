/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 20:17:49 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/31 21:28:49 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_trim_len(char const *s1, int len, char const *set)
{
	int	i;

	i = 0;
	while (set[i])
	{
		if (s1[len - 1] == set[i])
		{
			len--;
			i = 0;
		}
		else
			i++;
	}
	return (len);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	len;
	int		i;

	i = 0;
	while (set[i])
	{
		if (s1[0] == set[i])
		{
			s1++;
			i = 0;
		}
		else
			i++;
	}
	len = ft_strlen(s1);
	i = 0;
	return (ft_substr(s1, 0, ft_trim_len(s1, len, set)));
}
