#include "push_swap.h"

int *fill_array(t_node *stacka, int size)
{
    int *arr;
    int i;

    i = 0;
    arr = malloc(size * sizeof(int));
    while (stacka)
    {
        arr[i++] = stacka->num;
        stacka = stacka->next;
    }
    return (arr);
}

void    ft_sort_array(int *arr, int size)
{
    int i;
    int j;
    int temp;

    i = 0;
    while (i < size -1)
    {
        j = i + 1;
        while (j < size)
        {
            if(arr[i] > arr[j])
            {
                tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
            j++;
        }
        i++;
    }
}

int ft_get_index(int *arr, int size, int num)
{
    int i;

    i = 0;
    while (i < size)
    {
        if (arr[i] == num)
            return (i);
        i++;
    }
    return (-1);
}

void    ft_index(t_node *stacka)
{
    int *arr;
    int size;

    size = ft_stack_size(stacka);
    arr = ft_fill_array(stacka, size);
    ft_sort_array(arr, size);

    while (stacka)
    {
        stacka->index = ft_get_index(arr, size, stacka->num);
        stacka = stacka->next;
    }
    free(arr);
}