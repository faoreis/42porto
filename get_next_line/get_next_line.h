/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 10:42:06 by faribeir          #+#    #+#             */
/*   Updated: 2025/12/04 20:42:24 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
#	define GET_NEXT_LINE_H
# 	ifndef BUFFER_SIZE
#  		define BUFFER_SIZE 42
# endif
# include <stdlib.h>
# include <unistd.h>
# include <fcntl.h>
# include <stdio.h>


char	*get_next_line(int fd);
char	*ft_strdup(const char *s);
int	ft_strlen(const char *s);
char	*ft_substr(const char *s, unsigned int start, size_t len);
char	*ft_strjoin(const char *s1,const char *s2);
static char *ft_line_buffer(int fd, char *stash, char *buffer);
static char	*ft_line(char *stash);
char	*ft_strchr(const char *s, int c);

#endif
