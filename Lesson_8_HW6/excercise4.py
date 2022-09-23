import random
from random import choice, shuffle


def create_chars_table():
    """creating list with chars for password in ascii codes"""
    chars = []
    chars_splitted_sets = [[], [], [ord('_')]]
    for i in range(ord('0'), ord('9')+1):
        chars.append(i)
        chars_splitted_sets[0].append(i)
    for i in range(ord('A'), ord('Z')+1):
        chars.append(i)
        chars_splitted_sets[1].append(i)
    for i in range(ord('a'), ord('z')+1):
        chars.append(i)
        chars_splitted_sets[2].append(i)
    return chars, chars_splitted_sets


def create_password():
    chars = create_chars_table()
    chars_splitted = chars[1]  # chars splitted by sets
    all_chars = chars[0]
    password_codes = []
    password = []
    while len(password_codes) < 5:  # first 5 digits we receive randomly from all chars
        password_codes.append(random.choice(all_chars))
    for i in chars_splitted:  # last 3 digits we get from corresponding char sets
        password_codes.append(random.choice(i))
    for i in password_codes:
        password.append(chr(i))
    random.shuffle(password)  # and shuffle them
    return password


def main():
    password = create_password()
    password_output= "".join(password)
    print(f"Ваш пароль:{password_output}")


if __name__ == "__main__":

    main()


