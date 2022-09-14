import random
from random import randint
number = randint(1, 100)


def guess_player():
    correct_answer = number
    question = int(input("Вгадайте число від 1 до 100:"))
    if question == correct_answer:
        print("Ви вгадали це", correct_answer)
        game_choice()
    elif question < 1 or question > 100:
        print("Ви маєте ввести ціле число від 1 до 100")
        guess_player()
    else:
        if question > correct_answer:
            print("Ви не вгадали, загадане число меньше")
            guess_player()
        elif question < correct_answer:
            print("Ви не вгадали, загадане число більше")
            guess_player()


def guess_comp():
    print("Ще не готово")
    return main()

def game_choice():
    welcome_txt = f"Бажаєете грати ще раз?\nВведить ТАК для подальшої гри чи НІ для завершення\nТАК/НІ:"
    choice = str(input(welcome_txt))
    if choice == "ТАК":
        main()
    elif choice == "НІ":
        pass

def main():
    welcome_txt = f"     Оберить тип гри\nВгадує гравец    (натиснить 1) \nВгадує комп'ютер (натиснить 2)" \
                  f"\nДля виходу       (натиснить 3)\n1/2/3?:"
    main_choice = int(input(welcome_txt))
    if main_choice == 1:
        guess_player()
    elif main_choice == 2:
        guess_comp()
    elif main_choice == 3:
        pass
    else:
        main()


if __name__ == main():

    main()


