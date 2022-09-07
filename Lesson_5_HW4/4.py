number = int(input("Введить рік:"))


def year_check(number):
    if number % 400 == 0:
        return "YES"
    elif number % 100 == 0:
        return "NO"
    elif number % 4 == 0:
        return "YES"

    else:
        return "NO"


print(year_check(number))
