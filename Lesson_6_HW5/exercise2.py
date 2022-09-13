import random
from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    number_list = [[randint(lower_bound, upper_bound) for _ in range(num_limit)]]

    return max(number_list[0]) - min(number_list[0])


print(diff_min_max(10, 1, 100))
