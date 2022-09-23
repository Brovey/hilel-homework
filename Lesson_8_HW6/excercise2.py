def copy_deep(lst):
    list_new= []
    for i in list1:
        if isinstance(i, list):
                list_new.append(i[:])
        else:
            list_new.append(i)
    return list_new


list1 = [1, 2, 3, ["a", "b"]]
list_new = copy_deep(list1)


