/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/12 21:04:11 by faribeir          #+#    #+#             */
/*   Updated: 2026/02/14 10:13:19 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_strcmp(const char *s1, const char *s2)
{
	while (i < n - 1 && s1[i] == s2[i] && s1[i] && s2[i])
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}


int	ft_contains(const char *s1, const char **s2, int i)
{
	int	compar;

	compar = 1;
	i++;
	while (s2[i] && compar != 0)
	{
		compar = ft_strcmp(s1, s2[i]);
	}
	if (compar == 0)
		return (1);
	else
		return (0);
}

int	ft_validade_num(char **num, int i)
{
	int	lerror;
	int tempnum;

	lerror = 0;
	while (num[i] && !lerror)
	{
		lerror = ft_isnum(num[i]);
		if (!lerror)
			lerror = ft_contains(num[i], num, i);
		if (!lerror)
		{
			tempnum = ft_atoi(num[i]);
			if (tempnum < -2147483648 || tempnum > 2147483647)
				lerror = 1;
		}		
	}
	return (lerror);
}

int    ft_validate_arg(int argc, char **argv)
{
	int	i;
	char **list;
	int lerror;

	i = 0;
	if(argc == 2)
		list = ft_split(argv[1], ' ');
	else
	{
		list = argv;
		i = 1;
	}
	lerror = ft_validade_num(list, i);
	if (lerror)
	{
		if (argc == 2)
			ft_free(list);
		ft_error("Error");
	}
		
}
   
int main(int argc,char **argv)
{

	if(argc == 1)   
		return (0); 
	ft_validate_arg(argc, list);
	/*
		if(argc == 2)
		list = ft_split(argv[1], ' ');
	else
		list = argv;  
	error = ft_validate_arg(argc, list);
	if (error < 0)
		return (write(1, "error\n", 6));
	else
		return (write(1, "ok!", 3));
	return 0;
	*/
}   
