/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/25 14:38:36 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/25 16:22:07 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_lenint(int n)
{
	int				len;
	unsigned int	i;

	len = 0;
	if (n < 0)
	{
		len++;
		i = -(n);
	}
	else
		i = n;
	while (i > 9)
	{
		i = i / 10;
		len++;
	}
	len++;
	return (len);
}

void	ft_convert(char *str, int n, int len)
{
	unsigned int	i;

	if (n < 0)
	{
		str[0] = '-';
		i = -(n);
	}
	else
		i = n;
	if (i <= 9)
		str[len - 1] = i + '0';
	else
	{
		ft_convert(str, i / 10, len -1);
		str[len - 1] = (i % 10) + '0';
	}
}

char	*ft_itoa(int n)
{
	char	*str;
	int		len;

	len = ft_lenint(n);
	str = malloc((len + 1) * sizeof(char));
	if (!(str))
		return (NULL);
	ft_convert(str, n, len);
	str[len] = '\0';
	return (str);
}
