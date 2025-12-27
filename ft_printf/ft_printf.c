/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 11:12:40 by faribeir          #+#    #+#             */
/*   Updated: 2025/12/27 11:47:54 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h" 

int	ft_putnbr_u(unsigned int nbr)
{
	int	count;

	count = 0;
	if (nbr < 10)
		return (count += ft_putchar(nbr + '0'));
	else
	{
		count += ft_putnbr(nbr / 10);
		count += ft_putchar((nbr % 10) + '0');
	}
	return (count);
}

int	ft_var_type(const char *str, va_list args, int *i)
{
	if (str[*i] == 'c')
		return (ft_putchar(va_arg(args, int)));
	else if (str[*i] == 's')
		return (ft_putstr(va_arg(args, char *)));
	else if (str[*i] == '%')
		return (ft_putchar('%'));
	else if (str[*i] == 'd' || str[*i] == 'i')
		return (ft_putnbr(va_arg(args, int)));
	else if (str[*i] == 'u')
		return (ft_putnbr_u(va_arg(args, unsigned int)));
	else if (str[*i] == 'p')
		return (ft_put_pointer(va_arg(args, void *)));
	else if (str[*i] == 'x' || str[*i] == 'X')
		return (ft_putnbr_base(va_arg(args, unsigned int), str[*i]));
	return (0);
}

int	ft_print(char const *str, va_list args)
{
	int	i;
	int	count;

	i = 0;
	count = 0;
	while (str[i])
	{
		if (str[i] != '%')
			count += ft_putchar(str[i]);
		else
		{
			i++;
			count += ft_var_type(str, args, &i);
		}
		i++;
	}
	return (count);
}

int	ft_printf(const char *str, ...)
{
	va_list	args;
	int		len;

	len = 0;
	va_start(args, str);
	len = ft_print(str, args);
	va_end(args);
	return (len);
}

/*
int	main(void)
{
	char	*str = "world hello";
	char *s2 = "Mussum Ipsum, caciilds vidis litro abertis. Posuerro vreus.";
	int	numc;
	char	c = 'S';
	int	i = (-9468597);

	numc = ft_printf(" %s %s %s %s %s", " - ", "", "4", "", s2);
	printf("\n");
	printf("%d\n", numc);
	numc = ft_printf("Hello world: %c\n", c);
	printf("%d\n", numc);

	numc = ft_printf("Hello world: %s\n", str);
	printf("%d\n", numc);
	printf("%%\n");
	numc = ft_printf("Hello world: %d\n", i);
        printf("%d\n", numc);
	return (0);
}
*/
