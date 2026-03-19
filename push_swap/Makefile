# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: faribeir <faribeir@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/19 21:33:46 by faribeir          #+#    #+#              #
#    Updated: 2026/03/19 22:28:23 by faribeir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap
CC = cc
CFLAGS = -g -Werror -Wall -Wextra 

RM = rm -rf

SRCS =  push_swap.c \
	create_stack.c \
	index.c \
	ft_chunk.c \
	sort.c \
	operations/*.c \
	Libft/libft.a \

$(NAME) :
	make bonus -C Libft
	cc $(CFLAGS) $(SRCS) -o $(NAME)

all : $(NAME)

fclean : clean
	$(RM) $(NAME)
	make fclean -C Libft

clean :
	make clean -C Libft

re : fclean all

