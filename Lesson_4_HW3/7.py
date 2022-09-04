number = str(input("Введить трьохзначне число: "))


def my_sum(number):
    """ Sum of 3 digits received as str,  using ASCII values"""

    zero_ascii = ord("0")
    first_digit = ord(number[0]) - zero_ascii
    second_digit = ord(number[1]) - zero_ascii
    third_digit = ord(number[2]) - zero_ascii
    return first_digit + second_digit + third_digit


print(my_sum(number))




