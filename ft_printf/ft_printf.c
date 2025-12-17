/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 11:12:40 by faribeir          #+#    #+#             */
/*   Updated: 2025/12/16 20:01:52 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h" 

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

int	main(void)
{
	char	*str = "world hello";
	int	numc;
	char	c = 'S';
	int	i = (-9468597);

	numc = ft_printf("Hello world: %c\n", c);
	printf("%d\n", numc);
	numc = ft_printf("Hello world: %s\n", str);
	printf("%d\n", numc);
	printf("%%\n");
	numc = ft_printf("Hello world: %d\n", i);
        printf("%d\n", numc);
	return (0);
}
