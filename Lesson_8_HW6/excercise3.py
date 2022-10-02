list1 = [5, '9', 0, '452', 6.5, '6', 1, 2, 99]
list2 = [472, 326, 1, '1101000', 99, '9', '20', 863, '0']



def key(i):
    """My crazy solution via lists"""
    elem = list(map(int, str(i)))
    return elem[0]


newlist1 = sorted(list1, key=lambda i: float(i))  # with lambda function
newlist2 = sorted(list2, key=lambda i: str(i)[0])

print(f'{newlist1},\n{newlist2}')

