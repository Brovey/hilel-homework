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

print(create_chess())

# for i in range(first_digit, last_digit):
#    number_list.append(i)