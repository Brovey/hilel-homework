"""""
def my_funct():
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
"""


phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321"},
              {"name": "Oleg", "surname": "Sidorov", "age": 50, "phone_number":"+380507554555"},
              {"name": "Oleg", "surname": "Antonov", "age": 25, "phone_number":"+380507554556"}
             ]


new_phone_book = sorted(phone_book, key=lambda i: i['age'] )

print(new_phone_book)