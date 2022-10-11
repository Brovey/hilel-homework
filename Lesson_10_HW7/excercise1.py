def copy_deep(any_set):
    """Receive any of tuple, dict or list and return copy"""
    if isinstance(any_set, tuple):
        list_new = []
        for elem in any_set:
            list_new.append(copy_deep(elem))
        return tuple(list_new)
    if isinstance(any_set, list):
        list_new = []
        for elem in any_set:
            list_new.append(copy_deep(elem))
        return list_new
    if isinstance(any_set, dict):
        dict_new = {}
        for key, value in any_set.items():
            dict_new[copy_deep(key)] = copy_deep(value)
        return dict_new
    return any_set


tuple1 = (1, 2, [55,  ["test"], {"a": 1}, (1, 2, 3)])
dict1 = {'a': [(1, [2, 3], ([1, 2, 3], ))]}
list1 = [1, 2, ["a", "b", [1], {"a": 1}, (1, 2, 3)]]
copy = copy_deep(dict1)
print(f'copy     {copy}\noriginal {dict1}\n',  copy is dict1)


