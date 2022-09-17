def create_chess():
    """Funciton creates chessboard and according list with powers of 2 """
    letters = "abcdefgh"
    digits = "12345678"
    quantity_board = []
    chess_board = []
    for i in letters:
        for j in digits:
            chess_board.append(i+j)
    for i in range(64):
        quantity_board.append(2**i)
        i += 1
    return chess_board, quantity_board


def calculate_wheat_chess_position(kilograms):
    """Compares quantity of seeds with quantity_board and return corresponding index from chess_board   """
    boards = create_chess()
    quantity = kilograms / 0.000035
    chess_board = boards[0]
    quantity_board = boards[1]
    index = 0
    for idx, value in enumerate(quantity_board):
        if value <= quantity:
            index = idx
        else:
            break
    return chess_board[index]


def main():
    kilograms = float(input("Введить вагу в кг:"))
    print("Потрібна клітина це", calculate_wheat_chess_position(kilograms))


if __name__ == "__main__":

    main()
