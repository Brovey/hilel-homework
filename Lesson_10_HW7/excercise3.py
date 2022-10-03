import pickle


running = True

#------------------------------------------------------------------------------
phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567", "country": "Ukraine"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321", "country": "Ukraine"},
              {"name": "Oleg", "surname": "Sidorov", "age": 50, "phone_number":"+380507554555", "country": "Usa"},
              {"name": "Oleg", "surname": "Antonov", "age": 25, "phone_number":"+380507554556", "country": "Poland"}
             ]


#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    print ("| Country: %20s |" % entry["country"])
    print ()


#------------------------------------------------------------------------------
def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    index = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(index, entry)
            index += 1
            found = True
    if not found:
        printError("Not found!!")



#------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    del_name = str(input("    Enter name to delete entry: "))
    found = False
    for item in reversed(phone_book):
        for value in item.values():
            if value == del_name:
                index = phone_book.index(item)
                del phone_book[index]
                found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()
    new_phone_book = sorted(phone_book, key=lambda i: i['age'])
    number = 1
    for entry in new_phone_book:
        print_entry(number, entry)
        number += 1




#------------------------------------------------------------------------------
def increase_age():
    age_increase = int(input("    Enter years to increase age: "))
    for item in phone_book:
        for key, value in item.items():
            if key == "age":
                new_value = value + age_increase
                item.update({key: new_value})


    if len(phone_book) == 0:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_by_country():
    country = str(input("    Enter country: "))
    index = 1
    found = False
    for entry in phone_book:
        if entry["country"] == country:
            print_entry(index, entry)
            index += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def print_by_country():
    print()
    print()
    print("#########  Phone book  ##########")
    print()
    new_phone_book = sorted(phone_book, key=lambda i: i['country'])
    number = 1
    for entry in new_phone_book:
        print_entry(number, entry)
        number += 1



#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    average = 0
    for elements in phone_book:
        for key, value in elements.items():
            if key == "age":
                average += value

    print(f"Average age {round(average/len(phone_book))} years")


#------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


#------------------------------------------------------------------------------
def exit():
      global running
      running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     6 - Delete entry by name")
      print("     7 - The number of entries in the phonebook")
      print("     8 - Avr. age of all persons")
      print("     9 - Increase age by num. of years")
      print("     c - Find entry by country")
      print("     v - Print phonebook entries by country")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:

            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,
                  'c':  find_by_country,
                  'v':  print_by_country,

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
