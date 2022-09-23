list1 = [5, '9', 0, '452', 6.5, '6', 1, 2]
list2 = [472, 326, 1, '1101000', 9, '20', 863, '0']


def key(i):
    i = str(i)
    return i


newlist1 = sorted(list1, key=lambda i: float(i))  # with lambda function
newlist2 = sorted(list2, key=key)

print(f'{newlist1},\n{newlist2}')

