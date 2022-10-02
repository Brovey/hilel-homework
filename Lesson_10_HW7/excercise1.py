def copy_deep(any_set):
    """Receive any of tuple, dict or list and return copy"""
    list_new = []
    dict_new = {}
    if isinstance(any_set, tuple):
        new_tuple = any_set
        return new_tuple
    if isinstance(any_set, list):
        for elem in any_set:
            if isinstance(elem, list):
                list_new.append(copy_deep(elem))
            else:
                list_new.append(elem)
        return list_new
    if isinstance(any_set, dict):
        """"
        for cicle   showed by Artem as option  not working, i dont know why did same before and it was not ok:
        for key, value in any_set.items():
            dict_new[key] = value
        """
        return {copy_deep(key): copy_deep(value) for key, value in any_set.items()}
    return any_set  # for dict





tuple1 = (1, 2, 3, [55, 55, 66, ["gg"]])
dict1 = {'5': 5, '6': [1, 2, 3, 4, 5, ["test nested list"]]}
list1 = [1, 2, 3, ["a", "b", [1]]]
copies = copy_deep(list1)
#  copies[3][2].append([777777])

print(copies, list1)
