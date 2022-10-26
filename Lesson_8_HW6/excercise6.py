import random
text = "Это пример текста для функции которая перемешивает буквы в словах кроеме первой и последней "


def permutate(text):  # returns permuted text
    splitted_text = text.split()
    permuted_text = []
    final = []
    #tmp_word = []

    for elem in splitted_text:
        shufled_words = []
        if len(elem) > 3:
            tmp_medium = elem[1:-1]
            splitted_medium = [tmp_medium[i:i + 3] for i in range(0, len(tmp_medium), 3)]
            #print(tmp_medium, splitted_medium)
            for i in splitted_medium:
                tmp_shufle = random.sample(i, len(i))
                shufled_words.append(tmp_shufle)

            shufled_words.insert(0, elem[0])  # adding 1st elem from word
            shufled_words.append(elem[-1])    # adding last elem from word
            print(tmp_medium, splitted_medium, shufled_words)

            #shuf_medium = random.sample(i[1:-1], len(i[1:-1]))
            #shuf_medium.insert(0, i[0])
            #shuf_medium.append(i[-1])
            #permuted_text.append(shuf_medium)
        else:
            permuted_text.append(elem)
    for i in permuted_text:
        word = "".join(i)
        final.append(word)
    return " ".join(final)


print(permutate(text))
