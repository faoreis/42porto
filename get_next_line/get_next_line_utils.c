/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 11:14:01 by faribeir          #+#    #+#             */
/*   Updated: 2025/12/06 16:28:01 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_strchr(const char *s, int c)
{
	unsigned char	i;

	i = c;
	while (*s != '\0')
	{
		if (*s == i)
			return ((char *)s);
		s++;
	}
	if (i == '\0')
		return ((char *)s);
	return (NULL);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char			*substr;
	unsigned int	i;
	unsigned int	slen;

	i = 0;
	slen = ft_strlen(s);
	if (slen < start)
		return (ft_strdup(""));
	if ((slen - start) < len)
		len = (slen - start);
	substr = malloc((len) + 1);
	if (!substr)
		return (NULL);
	while (i < len && s[start + i])
	{
		substr[i] = s[start + i];
		i++;
	}
	substr[i] = '\0';
	return (substr);
}

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

int	ft_strlen(const char *s)
{
	int	i;

	i = 0;
	while (s[i] != '\0')
		i++;
	return (i);
}

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
