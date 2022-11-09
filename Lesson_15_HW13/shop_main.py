from my_libs import *

storage = Storage()
menu = MainMenu()
files = WorkWithFile()


def main():
    while True:
        menu.print_menu()
        menu_call = str(input("Enter menu #:"))
        if menu_call == "1":
            storage.add_item_manually()
        elif menu_call == "2":
            storage.add_product_to_storage()
        elif menu_call == "3":
            storage.sell_product()
        elif menu_call == "4":
            storage.print_income()
        elif menu_call == "5":
            storage.print_database()
        elif menu_call == "s":
            files.save_to_file(storage.create_output_data())
        elif menu_call == "l":
            files.load_from_file()
            storage.loading_to_storage(files.load_from_file())
        elif menu_call == "0":
            exit()
        else:
            print("Wrong choice,  try again")


if __name__ == '__main__':
    main()
