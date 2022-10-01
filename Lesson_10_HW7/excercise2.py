def lchain(*args):  # returns list
    new_list = []
    for i in args:
        for k in i:
            new_list.append(k)
    return new_list


print(lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))
