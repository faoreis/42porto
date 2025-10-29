/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/25 14:38:36 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/29 22:16:41 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>
static int	ft_lenint(int n)
{
	int				len;
	unsigned int	i;

	len = 0;
	if (n < 0)
	{
		len++;
		i = -n;
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

static void	ft_convert(char *str, unsigned int n, int len)
{
	if (n <= 9)
		str[len - 1] = n + '0';
	else
	{
		ft_convert(str, n / 10, len -1);
		str[len - 1] = (n % 10) + '0';
	}
}

char	*ft_itoa(int n)
{
	char				*str;
	int		len;
	unsigned int		i;

	len = ft_lenint(n);
	str = ft_calloc((len + 1), sizeof(char));
	if (!(str))
		return (NULL);
	if (n < 0)
	{
		str[0] = '-';
		i = -n;
	}
	else
		i = n;
	ft_convert(str, i, len);
	str[len] = '\0';
	return (str);
}
/*

int     main(void)
{
	char *str = ft_itoa(-623);
        printf("%s", str);
	free(str);
        return (0);
}
*/
