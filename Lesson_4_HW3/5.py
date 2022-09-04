my_string = str(input("Введить рядок:"))


def string_things(my_string):
    print(my_string[2])  # 3rd symbol
    print(my_string[-2])  # 2nd symbol from the end
    print(my_string[0:5])  # first five symbols
    print(my_string[0:-2])  # except last two
    print(my_string[0::2])  # only even indexes
    print(my_string[1::2])  # only odd indexes
    print(my_string[::-1])  # reversed
    print(my_string[::-2])  # reversed  through one
    print(len(my_string))  # length



string_things(my_string)
