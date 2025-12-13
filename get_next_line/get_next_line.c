/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 20:31:11 by faribeir          #+#    #+#             */
/*   Updated: 2025/12/06 16:31:05 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_line(char *stash)
{
	char	*final;
	ssize_t	i;

	i = 0;
	while (stash[i] != '\n' && stash[i] != '\0')
		i++;
	if (stash[i] == '\0')
		return (NULL);
	final = ft_substr(stash, i + 1, ft_strlen(stash) - 1);
	if (final[0] == '\0')
	{
		free(final);
		final = NULL;
	}
	stash[i + 1] = '\0';
	return (final);
}

char	*ft_line_buffer(int fd, char *stash, char *buffer)
{
	ssize_t	readbyte;
	char	*temp;

	readbyte = 1;
	while (readbyte > 0)
	{
		readbyte = read(fd, buffer, BUFFER_SIZE);
		if (readbyte < 0)
		{
			free(stash);
			return (NULL);
		}
		else if (readbyte == 0)
			break ;
		buffer[readbyte] = '\0';
		if (!stash)
			stash = ft_strdup("");
		temp = stash;
		stash = ft_strjoin(temp, buffer);
		free(temp);
		if (ft_strchr(stash, '\n'))
			break ;
	}
	return (stash);
}

char	*get_next_line(int fd)
{
	static char	*stash;
	char		*buffer;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (NULL);
	line = ft_line_buffer(fd, stash, buffer);
	free(buffer);
	if (!line)
		return (NULL);
	stash = ft_line(line);
	return (line);
}

/*
int	main(void)
{
	int	fd;
	char	*line;
	int	i;

	i = 0;
	fd = open("big_line_with_nl", O_RDONLY);
	if (fd < 0)
	{
		perror("Erro ao abrir o ficheiro");
		return (1);
	}

	while (i < 20)
	{
		if(line = get_next_line(fd))
		{
			printf("line: %s\n", line);
			//free(line);
		}
		i++;
	}

	close(fd);
	return (0);
}
*/
