#  using string
MyNumber = str(input("введить трьохзначне число:"))
a, b, c = int(MyNumber[0]), int(MyNumber[1]), int(MyNumber[2])
print(a+b+c)



#  using list
MyNumber2 = input("введить трьохзначне число:")
NumList = [int(MyNumber2[0]), int(MyNumber2[1]), int(MyNumber2[2])]
print(sum(NumList))

# or
NumList = list(map(int, MyNumber))# used map to get list with integers
print(sum(NumList))


