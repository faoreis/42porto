/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 20:31:11 by faribeir          #+#    #+#             */
/*   Updated: 2025/11/18 21:04:33 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

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

int	ft_strlen(char *s)
{
	int	i;

	i = 0;
	while (s[i] != '\0')
		i++;
	return (i);
}

char *ft_check_line(char *buffer, char *stash)
{
	char	*final;
	char	*line;

	final = ft_strchr(buffer, '\n');
	if(final)
	{
		line = ft_substr(buffer, 0 , ft_strlen(buffer) - ft_strlen(final));
		if(!line)
			return (NULL);
		stash = ft_strjoin(stash, final);
		return(line);
	}
	else
	{
		stash = ft_strjoin(stash, buffer);
		return (NULL);
	}
}

char	*get_next_line(int fd)
{
	static char	*stash;
	char	*buffer;
	int	readbyte;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (NULL);
	while ((readbyte = read(fd, buffer, BUFFER_SIZE)) > 0)
	{

	}
}
