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

void	ft_free_all(char **strs, int i)
{
	while (i >= 0)
	{
		free(strs[i]);
		i--;
	}
	free(strs);
}

int	ft_alloword(char **strs, char c, char const *s)
{
	int	i;
	int	len;

	i = 0;
	while (*s)
	{
		while (*s == c && *s)
			s++;
		if (*s)
		{
			len = 0;
			while (s[len] && s[len] != c)
				len++;
			strs[i] = ft_substr(s, 0, len);
			if (strs[i] == NULL)
			{
				ft_free_all(strs, i);
				return (0);
			}
			i++;
			s += len;
		}
	}
	strs[i] = NULL;
	return (1);
}

char	**ft_split(char const *s, char c)
{
	char	**strs;

	strs = malloc((ft_coustring(s, c) + 1) * sizeof(char *));
	if (!(strs))
		return (NULL);
	if (!ft_alloword(strs, c, s))
		return (NULL);
	return (strs);
}
