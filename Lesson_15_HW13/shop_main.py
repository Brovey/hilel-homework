import csv


class Storage:

    def __init__(self):
        self.storage = {}
        self.total_income = 0

    def print_income(self):
        temp_total = 0
        for key in self.storage.keys():
            temp_total += self.storage[key][5]
        print("----------------")
        print('Already sold:')
        for key in self.storage:
            print(f'{self.storage[key][0]} for  {self.storage[key][5]} UAH')
        print("----------------")
        print('Products left in stock')
        for key in self.storage:
            print(f'{self.storage[key][0]}  = {self.storage[key][3]}')
        print("----------------")
        print(f'Total income for all sold items:  {temp_total} UAH')

    def add_item_manually(self):
        item_id = str(input("Enter item id:"))
        if item_id in self.storage:
            print("This item id already in database")
        item_name = str(input("Enter item name:"))
        item_price = int(input("Enter item price:"))
        item_category = str(input("Enter item category:"))
        item_quantity, items_sold, item_income = 0, 0, 0
        item_details = [item_name, item_price, item_category, item_quantity, items_sold, item_income]
        self.storage[item_id] = item_details
        print(f'You added new item {item_name} to category {item_category} in database')

    def add_product_to_storage(self):
        """Checks if id in storage if no adding new product else increasing its quantity"""
        product_id = str(input("Enter item id:"))
        quantity = int(input("Enter item quantity:"))
        if product_id in self.storage:
            for key in self.storage.keys():
                if key == product_id:
                    self.storage[key][3] += quantity
        else:
            print("This item  id not in data base. Add it first  ")

    def sell_product(self):
        sell_item = str(input("Enter item id  to sell:"))
        sell_quantity = int(input("Enter how many items you want to sell:"))
        if sell_item in self.storage:

            for key in self.storage.keys():
                if sell_item == key:
                    self.storage[key][3] -= sell_quantity
                    self.storage[key][4] += sell_quantity
                    self.storage[key][5] += sell_quantity * self.storage[key][1]
                    break
        else:
            print("This item id  not in data base. Add it first  ")

    def create_output_data(self):
        output_list = []
        for k, v in self.storage.items():
            output_list.append(
                {"Item ID": k[0], "Item Name": v[0], "Item Price": v[1], "Category": v[2], 'Quantity': v[3],
                 'Sold items': v[4], 'Income by item': v[5]}
            )
        return output_list

    def loading_to_storage(self, input_data):
        self.storage = {k: v for elem in input_data for k, v in elem.items()}  # converting list of dict to dict

    def print_database(self):
        print(self.storage)


class MainMenu:
    def __init__(self, running=True):
        self.running = running

    def print_menu(self):
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("- 1. Add new product to database manually ")
        print("- 2. Add new product to storage ")
        print("- 3. Sell product")
        print("- 4. Income by products and total income ")
        print("- 5. Print product data base ")
        print("- s. Save to file")
        print("- l. Load from file")
        print("- 0. Exit                  ")
        print("--------------------------------------------")
        print("--------------------------------------------")


class WorkWithFile(Storage):
    def __init__(self):
        super().__init__()

    def save_to_file(self, output_data):
        with open('shop.csv', 'w', newline="") as my_file:
            fieldnames = ['Item ID', "Item Name", 'Item Price', 'Category', 'Quantity', 'Sold items', 'Income by item']
            writer = csv.DictWriter(my_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(output_data)

    def load_from_file(self):
        with open('shop.csv', 'r', newline='') as my_file:
            input_list = []
            reader = csv.DictReader(my_file)
            for k in reader:
                input_list.append(
                    {k["Item ID"]: [k["Item Name"], int(k['Item Price']), k['Category'], int(k['Quantity']),
                                    int(k['Sold items']), int(k['Income by item'])]}
                )
        return input_list


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
