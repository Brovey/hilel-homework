import random
from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound):  # returns int
    number_list = [randint(lower_bound, upper_bound) for _ in range(num_limit)]
    print(number_list)
    return max(number_list) - min(number_list)


print(diff_min_max(10, 1, 100))
