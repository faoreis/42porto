/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 21:20:02 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/14 19:23:05 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *str, int c, size_t n)
{
	unsigned char	*ptr;
	unsigned char	ca;
	size_t			i;

	i = 0;
	ptr = str;
	ca = c;
	while (i < n)
	{
		ptr[i] = ca;
		i++;
	}
	return (str);
}

/*
int	main(void)
{
	char str[] = "Welcome to Tutorialspoint";

	puts(str);

	memset(str, '#', 7);
	puts(str);
   
	return(0);
}
*/
