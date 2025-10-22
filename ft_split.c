/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: faribeir <faribeir@student.42porto.co      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 20:04:11 by faribeir          #+#    #+#             */
/*   Updated: 2025/10/22 19:10:00 by faribeir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_coustring(char const *s, char c)
{
	int	i;
	int	word;
	int	count;

	i = 0;
	count = 0;
	word = 0;
	while (s[i])
	{
		if (s[i] != c && !word)
		{
			word = 1;
			count++;
		}
		else if (s[i] == c)
			word = 0;
		i++;
	}
	return (count);
	
}

char	**ft_split(char const *s, char c)
{
	char	**strs;
	int	i;
	int	j;
	int	nstr;

	nstr = ft_coustring(s, c);
	strs = malloc((nstr + 1) * sizeof(char*));
	if (strs == NULL)
		return (NULL);
	while (s[i])
	{
		
	}
}
