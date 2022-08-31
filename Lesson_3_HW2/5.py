#  using string
MyNumber = str(input("введить трьохзначне число:"))
a, b, c = int(MyNumber[0]), int(MyNumber[1]), int(MyNumber[2])
print(a+b+c)

# using arithmetic operations
int_num = input("введить трьохзначне число:")
first_digit = int(int_num)//100
second_digit = int(int_num) % 100//10
third_digit = int(int_num) % 10
print(first_digit + second_digit + third_digit)


#  using list
#  MyNumber2 = input("введить трьохзначне число:")
#  NumList = [int(MyNumber2[0]), int(MyNumber2[1]), int(MyNumber2[2])]
#  print(sum(NumList))

# or
#  NumList = list(map(int, MyNumber))#  used map to get list with integers
#  print(sum(NumList))

