def copy_deep(lst):
    list_new= []
    for elem in lst:
        if isinstance(elem, list):
            list_new.append(copy_deep(elem))
        else:
            list_new.append(elem)
    return list_new


list1 = [1, 2, 3, ["a", "b", [1]]]
list_new = copy_deep(list1)

print(list1, list_new)