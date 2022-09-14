import random
from random import randint





def min_number(list):
    minimal = None # берем максимашльное число которое будет больше всех
    for elem in list:
        if minimal is None or elem < minimal:
            minimal = elem
    return minimal


def main():
    my_list = [randint(1, 100) for _ in range(12)]  # list compreh generate list
    minimal = min_number(my_list)


    print(my_list)
    print("min number", minimal)


if __name__ == main():
    main()



