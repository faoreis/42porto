#include "ft_printf.h" 

int ft_printf(const char *str, ...)
{
    va_list args;
    int i;
    int count;

    i = 0;
    count = 0
    va_start(args, str);
    while(str[i])
    {
        if (str[i] != '%')
        {
            ft_putchar(str[i]);
            count++;
        }
        else

    }
    va_end(args);
}