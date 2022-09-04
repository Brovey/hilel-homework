number = str(input("Введить трьохзначне число: "))


def my_sum(number):

    return (ord(number[0]) - ord("0")) + (ord(number[1]) - ord("0")) + (ord(number[2]) - ord("0"))


print(my_sum(number))




