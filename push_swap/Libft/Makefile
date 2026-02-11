# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/06 20:20:26 by faribeir          #+#    #+#              #
#    Updated: 2025/11/17 20:07:53 by faribeir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libft.a

FLAGS = -Wall -Wextra -Werror

OBJS = ft_putnbr_fd.o ft_putendl_fd.o ft_putstr_fd.o ft_putchar_fd.o ft_striteri.o ft_strmapi.o ft_itoa.o ft_split.o ft_strtrim.o ft_strjoin.o ft_substr.o ft_strdup.o ft_calloc.o ft_memmove.o ft_memcmp.o ft_memchr.o ft_atoi.o ft_strnstr.o ft_strncmp.o ft_strrchr.o ft_isprint.o ft_isalnum.o ft_isascii.o ft_strchr.o ft_strlcat.o ft_strlen.o ft_tolower.o ft_bzero.o ft_isalpha.o ft_isdigit.o ft_memcpy.o ft_memset.o ft_strlcpy.o ft_toupper.o

BONUS = ft_lstmap.o ft_lstiter.o ft_lstclear.o ft_lstnew.o ft_lstadd_front.o ft_lstsize.o ft_lstlast.o ft_lstadd_back.o ft_lstdelone.o

all: $(NAME)

bonus: $(BONUS) $(OBJS)
	ar -rc libft.a $(OBJS) $(BONUS)

$(NAME): $(OBJS)
	ar -rc libft.a $(OBJS)

%.o:%.c
	cc $(FLAGS) -c $< -I libft.h -o $@

clean:
	rm -rf $(OBJS) $(BONUS)

fclean: clean
	rm -rf libft.a

re: fclean all
