number = float(input("Введить число:"))


def sign_x(number):
    if number > 0:
        return 1
    elif number == 0:
        return 0
    else:
        return -1


def main():
    print(sign_x(number))


main()
