from math import sqrt

value1 = int(input("Введить значення першого катету:"))
value2 = int(input("Введить значення другого катету:"))
txt_square, txt_perim = "Площа трикутника:", "Периметр трикутника:"


def triangle_square_and_perimeter(a, b):  # returns 2 values
    """Receives values of two legs and returns square and perimetr of triangle """
    gipot = sqrt(a ** 2 + b ** 2)
    perimetr = a + b + gipot
    square = (a*b)/2
    return square, perimetr


print(f'{txt_square}{triangle_square_and_perimeter(value1, value2)[0]} \n'  # f-strings so good
      f'{txt_perim}{triangle_square_and_perimeter(value1, value2)[1]}')

