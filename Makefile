# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rodrmore <rodrmore@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/10 04:04:41 by rodrmore          #+#    #+#              #
#    Updated: 2025/10/27 22:02:30 by faribeir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
NAME = libft.a

FLAGS = -Wall -Wextra -Werror

OBJS = ft_putnbr_fd.o ft_putendl_fd.o ft_putstr_fd.o ft_putchar_fd.o ft_striteri.o ft_strmapi.o ft_itoa.o ft_split.o ft_strtrim.o ft_strjoin.o ft_substr.o ft_strdup.o ft_calloc.o ft_memmove.o ft_memcmp.o ft_memchr.o ft_atoi.o ft_strnstr.o ft_strncmp.o ft_strrchr.o ft_isprint.o ft_isalnum.o ft_isascii.o ft_strchr.o ft_strlcat.o ft_strlen.o ft_tolower.o ft_bzero.o ft_isalpha.o ft_isdigit.o ft_memcpy.o ft_memset.o ft_strlcpy.o ft_toupper.o

all: $(NAME)

bonus: $(BONUS) $(OBJS)
	ar -rc libft.a $(OBJS) $(BONUS)

$(NAME): $(OBJS)
	ar -rc libft.a $(OBJS)

%.o:%.c
	cc $(FLAGS) -c $< -I libft.h -o $@

clean:
	rm -rf $(OBJS)

fclean: clean
	rm -rf libft.a

re: fclean all
