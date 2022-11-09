import random
text = "Это пример текста для функции которая перемешивает буквы в словах кроеме первой и последней "


def permutate(text):  # returns permuted text
    splitted_text = text.split()
    permuted_text = []
    final = []

    for i in splitted_text:
        if len(i) > 3:
            shuf_medium = random.sample(i[1:-1], len(i[1:-1]))
            shuf_medium.insert(0, i[0])
            shuf_medium.append(i[-1])
            permuted_text.append(shuf_medium)
        else:
            permuted_text.append(i)
    for i in permuted_text:
        word = "".join(i)
        final.append(word)
    return " ".join(final)


print(permutate(text))
