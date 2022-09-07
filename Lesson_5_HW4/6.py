def fibonachi(number):
    if number <= 1:
        return number
    else:
        return fibonachi(number - 1) + fibonachi(number - 2)


print(fibonachi(20))
