def copy_deep(any_set):
    """Receive any of tuple, dict or list and return copy"""
    if isinstance(any_set, tuple):
        list_new = []
        for elem in any_set:
            if isinstance(elem, list):
                list_new.append(copy_deep(elem))
            else:
                list_new.append(elem)
        return tuple(list_new)
    if isinstance(any_set, list):
        list_new = []
        for elem in any_set:
            if isinstance(elem, list):
                list_new.append(copy_deep(elem))
            else:
                list_new.append(elem)
        return list_new
    if isinstance(any_set, dict):
        dict_new = {}  # problem was here  my dict_new = {}  was above all if statement
        for key, value in any_set.items():
            dict_new[key] = value
        return dict_new
    return any_set

tuple1 = (1, 2, 3, [55, 55, 66, ["gg"]])
dict1 = {'5': 5, '6': [1, 2, 3, 4, 5, ["test nested list"]]}
list1 = [1, 2, 3, ["a", "b", [1]]]
copy = copy_deep(list1)
#copy[3][2].append([777777])
#dict1 = {'5': 5, '6': [1, 2, 3, 4, 5, ["test nested list",[77777]]]}

print(copy, list1)
