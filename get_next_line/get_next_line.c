/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 20:31:11 by faribeir          #+#    #+#             */
/*   Updated: 2025/11/29 16:20:48 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_check_line(char *buffer, char *stash)
{
	char	*final;
	char	*line;
	char	*temp;

	if (!stash)
		temp = buffer;
	else
		temp = ft_strjoin(stash, buffer);
	final = ft_strchr(temp, '\n');
	if (final)
	{
		line = ft_substr(temp, 0, ft_strlen(temp) - ft_strlen(final));
		if (!line)
			return (NULL);
		stash = ft_substr(temp,ft_strlen(temp)- ft_strlen(final), ft_strlen(final));
		free(temp);
		return (line);
	}
	stash = temp;
	free(temp);
	return (NULL);
}

char	*get_next_line(int fd)
{
	static char	*stash;
	char		*buffer;
	int			readbyte;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (NULL);
	readbyte = 1;
	while (readbyte > 0)
	{
		readbyte = read(fd, buffer, BUFFER_SIZE);
		if (readbyte > 0)
		{
			buffer[readbyte] = '\0';
			line = ft_check_line(buffer, stash);
		}
		if (line)
		{
			free(buffer);
			return (line);
		}
		if (readbyte == 0)
			return (stash);
	}
	return (NULL);
}
