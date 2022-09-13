def create_chess():
    letters = "abcdefgh"
    digits = "12345678"
    quantity_board = [1, 2]
    chess_board = []
    power = 2
    for i in letters:
        for j in digits:
            chess_board.append(i+j)
    for i in range(64-1):
        quantity_board.append(2**power)
        power += 1

    return chess_board, quantity_board


def calculate_wheat_chess_position(kilograms):
    quantity = kilograms / 0.000035
    chess_board = create_chess()[0]
    quantity_board = create_chess()[1]
    index = 0
    for i in quantity_board:
        if i <= quantity:
            index = quantity_board.index(i)
    return chess_board[index]


def main():
    kilograms = float(input("Введить вагу в кг:"))
    print("Потрібна клітина це", calculate_wheat_chess_position(kilograms))


if __name__ == main():

    main()
