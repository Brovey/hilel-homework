from math import sqrt

value1 = int(input("Введить значення першого катету:"))
value2 = int(input("Введить значення другого катету:"))
def triangle_square_and_perimeter(a, b):  # returns 2 values
    gipot = sqrt(a**2 + b**2)
    perimetr = a + b + gipot
    square = (a*b)/2
    return square, perimetr

print(triangle_square_and_perimeter(value1,value2))

