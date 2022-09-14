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
    """Super bad search here still thinking """
    answer_number = randint(1, 10)
    welcome_text = input("Загадай число от 1 до 10\nВведи ТАК якщо загадав")
    if welcome_text == "ТАК":
        answer = input(f"Ти загадав число {answer_number} , якщо вірно то введи ТАК якщо число не вірне то введи"
                       f" БІЛЬШЕ якщо загадане число більше або МЕНЬШЕ якщо твое число  меньше")
        while answer_number != "ТАК":
            if answer == "БІЛЬШЕ":
                answer_number = randint((answer_number+1), 10)
                answer = input(f"Ти загадав число {answer_number} , якщо вірно то введи ТАК якщо число не вірне "
                               f"то введи БІЛЬШЕ якщо загадане число більше або МЕНЬШЕ якщо твое число  меньше")
            elif answer == "МЕНЬШЕ":
                answer_number = randint(1, (answer_number-1))
                answer = input(f"Ти загадав число {answer_number} , якщо вірно то введи ТАК якщо число не вірне "
                               f"то введи БІЛЬШЕ якщо загадане число більше або МЕНЬШЕ якщо твое число  меньше")
            else:
                print("Я вгадала")
                break

    game_choice()


def game_choice():
    welcome_txt = f"Бажаєете грати ще раз?\nВведить ТАК для подальшої гри чи НІ для завершення\nТАК/НІ:"
    choice = str(input(welcome_txt))
    if choice == "ТАК":
        main()
    elif choice == "НІ":
        pass


def main():
    welcome_txt = f"     Оберить тип гри\nВгадує гравец    (введить 1) \nВгадує комп'ютер (введить 2)" \
                  f"\nДля виходу       (введить 3)\n1/2/3?:"
    main_choice = int(input(welcome_txt))
    if main_choice == 1:
        guess_player()
    elif main_choice == 2:
        guess_comp()
    elif main_choice == 3:
        pass
    else:
        main()


if __name__ == "__main__":

    main()

