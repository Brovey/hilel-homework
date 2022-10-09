def custom_deepcopy(values):
    if isinstance(values, list):
        return list(map(custom_deepcopy, values))
    if isinstance(values, tuple):
        return tuple(map(custom_deepcopy, values))
    if isinstance(values, dict):
        return {
            custom_deepcopy(key): custom_deepcopy(value)
            for key, value in values.items()
        }
    return values


tuple1 = (1, 2, [55,  ["test"]])
dict1 = {'a': [(1, [2, 3], ([1, 2, 3], ))]}
list1 = [1, 2, ["a", "b", [1]]]
copy = custom_deepcopy(tuple1)
#print(f'copy     {copy}\noriginal {dict1}\n',  copy['a'] is dict1['a'])
#print(f'copy     {copy}\noriginal {list1}\n',  copy is list1)
#print(id(copy[2][2]), id(list1[2][2]))
print(f'copy     {copy}\noriginal {tuple1}\n',  copy is tuple1)
print(id(copy[2][0]), id(tuple1[2][0]))
