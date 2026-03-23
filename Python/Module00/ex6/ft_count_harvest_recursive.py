def ft_count_harvest_recursive():
    def ft_recursive(x):
        if x == 1:
            print("Day", x)
            return
        ft_recursive(x - 1)
        print("Day", x)
    x = int(input("Days until harvest: "))
    ft_recursive(x)
    print("Harvest time!")
