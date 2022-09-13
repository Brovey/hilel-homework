import random
from random import randint
number = randint(1, 10)


def main():
    correct_answer = number
    question = int(input("Вгадайте число від 1 до 10:"))
    if question == correct_answer:
        print("Ви вгадали це", correct_answer)
    else:
        if question > correct_answer:
            print("Ви не вгадали, загадане число меньше")
            main()
        elif question < correct_answer:
            print("Ви не вгадали, загадане число більше")
            main()


main()
