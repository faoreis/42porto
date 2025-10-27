/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 21:49:10 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/27 22:04:05 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	unsigned int	nb;
	char	c;

	if (n < 0)
	{
		write(fd, "-", 1);
		nb = -(n);
	}
	else
		nb = n;
	if  (nb >= 0 && nb <= 9)
	{
		c = nb + '0';
		write(fd, &c, 1);
	}
	else
	{
		ft_putnbr_fd(nb / 10, fd);
		c = (nb % 10) + '0';
		write(fd, &c, 1);
	}
}
