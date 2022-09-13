import random
from random import randint


def diff_odd_even(num_limit, lower_bound, upper_bound):  # returns int
    number_list = [randint(lower_bound, upper_bound) for _ in range(num_limit)]
    print(number_list)
    sum_even, sum_odd = 0, 0
    for i in number_list:
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    print(sum_even, sum_odd)
    return sum_even - sum_odd


print(diff_odd_even(10,1,5))