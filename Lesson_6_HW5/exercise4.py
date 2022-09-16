from random import randint
number = randint(1000000000000, 9999999999999)


def get_max_digit(number):  # returns int
    """Using string and method sorted """
    number_str = str(number)
    sorted_numbers = sorted(number_str, reverse=True)
    return int(sorted_numbers[0])


def get_max_digit_list(number):
    """Using list and iterations"""
    number_list = []
    while number != 0:
        number_list.insert(0, number % 10)  # used insert here to make  elements order  according to number
        number = number // 10
    max_digit = None
    for e in number_list:
        if max_digit is None or e > max_digit:
            max_digit = e

    return max_digit


print(get_max_digit(number))
print(get_max_digit_list(number))
