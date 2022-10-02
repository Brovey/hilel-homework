def my_funct():
    """на проверку на целое число"""
    number = None
    while number is None:
        raw_str= input("enter text")
        number = int(raw_str)
        if number <= 1:
            print("число должно быть целым")
            return None
        elif number > 10:
            print("Не больше 10")
            return None
        return number

print(my_funct())



