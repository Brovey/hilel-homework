
def index(lst, elem):  # returns integer or None
    if elem in lst:
        for i in range(0, len(lst)):
            if lst[i] == elem:
                return i
    else:
        return None


print(index(["qqq", ":", 1, 4, 3.2], ":"))
