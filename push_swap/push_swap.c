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

int    ft_validate_input(int argc, char **list)
{
	int     i;
	int	outresult;

	i = 1;
	if (argc == 2)
		i = 0;
	outresult = 1;
	while (list[i])
	{
		outresult = ft_atoi(list[i]);
		if (outresult < 0)
			break;
		i++;
	}
	return (outresult);
}
   
int main(int argc,char **argv)
{
	char    **list;
	int	error;

	if(argc == 1)   
		return (0); 
	if(argc == 2)
		list = ft_split(argv[1], ' ');
	else
	list = argv;  
	error = ft_validate_input(argc, list);
	if (error < 0)
		return (write(1, "error\n", 6));
	else
		return (write(1, "ok!", 3));
	return 0;
}   
