def copydeep(lst):
    list_new= []
    for i in list1:
        if isinstance(i, list):
                list_new.append(i[:])
        else:
            list_new.append(i)
    return list_new


list1 = [1, 2, 3, ["a", "b"]]
list_new = copydeep(list1)

print(list1 is list_new)
print(list1, list_new)
list1[3].append("c")
print(list1, list_new)
