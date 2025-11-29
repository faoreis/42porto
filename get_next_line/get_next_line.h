/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 10:42:06 by faribeir          #+#    #+#             */
/*   Updated: 2025/11/29 11:30:19 by faribeir         ###   ########.fr       */
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


char	*get_next_line(int fd);
char	*ft_strdup(const char *s);
int	ft_strlen(const char *s);
char	*ft_substr(const char *s, unsigned int start, size_t len);
char	*ft_strjoin(const char *s1,const char *s2);
char	*ft_check_line(char *buffer, char *stash);
char	*ft_strchr(const char *s, int c);

#endif
