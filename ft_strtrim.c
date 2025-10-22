/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 15:45:46 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/18 18:08:30 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*str;
	int	len;
	int	i;
	int	j;
	int	equal;
	int 	index;
	char	*strtrim;

	i = 0;
	equal = 0;
	index = 0;
	str = malloc(ft_strlen(s1) + 1);
	while (s1[i])
	{
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
		equal = 0;
		i++;
	}
	str[index] = '\0';
	len = (ft_strlen(str));
	strtrim = malloc(len + 1);
	ft_strlcpy(strtrim, str, len + 1);
	free(str);
	return (strtrim);
}
