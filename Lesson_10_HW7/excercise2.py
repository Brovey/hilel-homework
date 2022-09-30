def lchain(*iterables):  # returns list
    elems = zip(*iterables)
    new_list = []
    for i in elems:
        new_list.append(i)
    return new_list

result = lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10))
print(result)