/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 11:15:38 by faribeir          #+#    #+#             */
/*   Updated: 2025/12/13 14:56:22 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putchar(char c)
{
	write(1, &c, 1);
	return (1);
}

int	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		write(1, &str[i], 1);
		i++;
	}
	return (i);
}

int	ft_putnbr(int nbr)
{
	unsigned int	nb;
	int		count;

	count = 0;
	if (nbr < 0)
	{
		count += ft_putchar('-');
		nb = -nbr;
	}
	else
		nb = nbr;
	if (nb < 10)
		return (count += ft_putchar(nb + '0'));
	else
	{
		count += ft_putnbr(nb / 10);
		count += ft_putchar((nb % 10) + '0');
	}
	return (count);
}

int	ft_putpointer(void *pointer)
{
	int	count;

	count = 0;
	count = ft_putstr("0x");


}

int	ft_putnbr_base()
