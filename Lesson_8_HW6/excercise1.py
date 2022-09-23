
def index(lst, elem):  # returns integer or None
    if elem in lst:
        return lst.index(elem)
    else:
        return None


print(index(["qqq", ":", 1, 4, 3.2], ":"))
