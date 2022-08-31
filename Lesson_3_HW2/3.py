word = str(input("Введить назву:"))
word2 = word.split("_")
a, b, c = str(word2[0]), str(word2[1]), str(word2[2])
NewWord = a.capitalize() + b.capitalize() + c.capitalize()
print(NewWord)

