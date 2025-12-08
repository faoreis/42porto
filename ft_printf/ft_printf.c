#include "ft_printf.h" 

int ft_print(char const *str, va_list args)
{
    int i;
    int count;

    i = 0;
    count = 0;
    while(str[i])
    {
        if (str[i] != '%')
        {
            ft_putchar(str[i]);
            count++;
        }
        else
        {
            i++;
            count += ft_var_type(str, args, i);
            i++;
        }
    }
}

int ft_printf(const char *str, ...)
{
    va_list args;
    int len;

    len = 0;
    va_start(args, str);
    len = ft_print(str, args);
    va_end(args);
    return (len)
}