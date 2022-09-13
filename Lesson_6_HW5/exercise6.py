def sum_symbol_codes(first, last):  # returns int
    first_symbol_ord = ord(first)
    last_symbol_ord = ord(last)
    check_ord = first_symbol_ord
    codes = [first_symbol_ord]
    while check_ord < last_symbol_ord:
        codes.append(first_symbol_ord+1)
        first_symbol_ord += 1
        check_ord += 1

    return sum(codes)


print(sum_symbol_codes("0", "6"))

