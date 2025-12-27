/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 11:15:38 by faribeir          #+#    #+#             */
/*   Updated: 2025/12/27 11:31:08 by faribeir         ###   ########.fr       */
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
	if (!str)
	{
		write(1, "(null)", 6);
		return (6);
	}
	while (str[i])
	{
		write(1, &str[i], 1);
		i++;
	}
	return (i);
}

int	ft_putnbr(int nbr)
{
	int				count;
	unsigned int	nb;

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

int	ft_put_pointer(void *pointer)
{
	int	count;

	count = 0;
	if ((unsigned long)pointer == 0)
	{
		write(1, "(nil)", 5);
		count += 5;
		return (count);
	}
	count += ft_putstr("0x");
	count += ft_putnbr_base((unsigned long)pointer, 'x');
	return (count);
}

int	ft_putnbr_base(unsigned long nbr, char c)
{
	int				count;
	char			*base;

	count = 0;
	if (c == 'x')
		base = "0123456789abcdef";
	else
		base = "0123456789ABCDEF";
	if (nbr < 16)
		return (count += ft_putchar(base[nbr]));
	else
	{
		count += ft_putnbr_base(nbr / 16, c);
		count += ft_putchar(base[nbr % 16]);
	}
	return (count);
}
