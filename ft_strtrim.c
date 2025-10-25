/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 15:45:46 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/25 10:27:21 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_trim(char *str, char const *s1, char const *set)
{
	int	i;
	int	j;
	int	equal;
	int	index;

	i = 0;
	index = 0;
	while (s1[i])
	{
		equal = 0;
		j = 0;
		while (set[j] && !equal)
		{
			if (s1[i] == set[j])
				equal = 1;
			j++;
		}
		if (!equal)
		{
			str[index] = s1[i];
			index++;
		}
		i++;
	}
	str[index] = '\0';
}

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*str;
	int		len;
	char	*strtrim;

	str = malloc(ft_strlen(s1) + 1);
	ft_trim(str, s1, set);
	len = (ft_strlen(str));
	strtrim = malloc(len + 1);
	ft_strlcpy(strtrim, str, len + 1);
	free(str);
	return (strtrim);
}
