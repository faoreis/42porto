/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 11:16:20 by faribeir          #+#    #+#             */
/*   Updated: 2025/12/27 11:40:35 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdio.h>

int	ft_putchar(char c);
int	ft_printf(const char *str, ...);
int	ft_var_type(const char *str, va_list args, int *i);
int	ft_print(char const *str, va_list args);
int	ft_putstr(char *str);
int	ft_putnbr(int nbr);
int	ft_putnbr_base(unsigned long nbr, char c);
int	ft_put_pointer(void *pointer);
int	ft_putnbr_u(unsigned int nbr);

#endif
