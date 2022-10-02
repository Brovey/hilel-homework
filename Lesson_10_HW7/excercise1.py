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
        for value in any_set:
            for values in any_set.values():
                if not isinstance(values, list):
                    dict_new[value] = any_set[value]

                else:
                    dict_new[value] = copy_deep(any_set[value])

        return dict_new


tuple1 = (1, 2, 3, [55, 55, 66, ["gg"]])
dict1 = {'5': 5, '6': [1, 2, 3, 4, 5, ["test nested list"]]}
list1 = [1, 2, 3, ["a", "b", [1]]]
copies = copy_deep(dict1)
copies['6'] = [1, 2, 3, 4, 5, ["test nested list"],777777]
print(copies, dict1)
