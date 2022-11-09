def copy_deep(any_set):
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
