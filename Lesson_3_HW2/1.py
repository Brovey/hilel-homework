#  a
a = "Hello"
b = "World"
c = a
a = b
b = c
print(a, b)

#  b
a = "Hello"
b = 2022
a, b = b, a
print(a, b)

#  c
a, b = 1, 200
a = a + b
b = a - b
a = a - b
print(a, b)
