char **ft_validate_input(int argc, char **list)
{
    int i;

    i = 1;
    if(argc == 2)
        i = 0;
    
}

int main(int argc,char **argv)
{
    char    **list;

    if(argc == 1)
        return (0);
    if(argc == 2)
        list = ft_split(argv[1], ' ');
    else
        list = argv;
    //ft_validate_input(argc, list);
    return 0;
}