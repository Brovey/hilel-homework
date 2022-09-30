def copy_deep(my_tuple=None, my_set=None):
    tmp_list = []
    tmp_set = {}
    if my_tuple is not None:
        for i in my_tuple:
            tmp_list.append(i)

    if my_set is not None:
        for i in my_set:
            if isinstance(i, list):
                tmp_set[i] = my_set[copy_deep(i)]
            else:
                for i in my_set:
                    tmp_set[i] = my_set[i]
    return tuple(tmp_list), tmp_set


tupple1 = (1, 2, 3, [55, 55, 66, ["gg"]])
set1 = {'5': 5, '6': [1, 2, 3, 4, 5]}
copies = copy_deep(tupple1,set1)
set1 = {'5': 5, '6': [1, 2, 3, 4, 5]}
print(f'Оригинал кортежа{tupple1}\nКопия кортежа{copies[0]}\nОригинал словаря {set1}\nКопия словаря {copies[1]}')