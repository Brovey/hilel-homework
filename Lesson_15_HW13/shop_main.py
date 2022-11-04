class Product:
    def __init__(self, price, product_name, product_id, category):
        self.price = price
        self.product_name = product_name
        self.category = category
        self.product_id = product_id

    def print_product(self):
        print("Product summary")
        print("---------------")
        print(f"Category: {self.category}\nName: {self.product_name}\n"
              f"Id: {self.product_id}\nPrice: {self.price} uah ")

    def return_product(self):
        """returns product in dict"""
        product_dict = {self.product_id: (self.product_name, self.price, self.category)}
        print(product_dict)
        return product_dict


class Storage:

    def __init__(self):
        self.income_by_item = {}  # keeping items id and their income
        self.storage = {}  # keeping items id and their limits
        self.total_income = 0
        self.data_base = {}  # keeping items info

    def print_income(self):
        print(f'Already sold:')
        for key in self.income_by_item:
            print(f'{self.storage[key][0]} for  {self.income_by_item[key]} UAH')
        print(f'Total income {self.total_income}')

    def add_item_manually(self):
        item_id = str(input("Enter item id:"))
        if item_id in self.data_base:
            print("This item id already in database")
        item_name = str(input("Enter item name:"))
        item_price = int(input("Enter item price:"))
        item_category = str(input("Enter item category:"))
        item_details = [item_name, item_price, item_category]
        self.data_base[item_id] = item_details
        print(self.data_base)
        print(f'You added new item {item_name} to category {item_category} in database')

    def add_product_to_storage(self):
        """Checks if id in storage if no adding new product else increasing its quantity"""
        product_id = str(input("Enter item id:"))
        quantity = int(input("Enter item quantity:"))
        if product_id not in self.storage:
            self.storage[product_id] = quantity  # adding new item id to storage
            self.income_by_item[product_id] = 0  # adding new item id to income_by_item
        else:
            for key in self.storage.keys():
                if key == product_id:
                    self.storage[key] += quantity

    def sell_product(self):
        sell_item = str(input("Enter item id  to sell:"))
        sell_quantity = int(input("Enter how many items you want to sell:"))
        for key in self.storage.keys():
            if sell_item == key:
                self.storage[key] -= sell_quantity
                break
        for key in self.income_by_item.keys():
            if sell_item == key:
                self.income_by_item[key] += sell_quantity * self.data_base[key][1]
                self.total_income += sell_quantity * self.data_base[key][1]
                break


class MainMenu:
    def __init__(self, running=True):
        self.running = running

    def print_menu(self):
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("- 1. Add new product to database ")
        print("- 2. Add new product to storage ")
        print("- 3. Sell product")
        print("- 4. Income by products and total income ")
        print("- Save to file")
        print("- Load from file")
        print("- 5. Print product limits   ")
        print("- 0. Exit                  ")
        print("--------------------------------------------")
        print("--------------------------------------------")

    def intermediate_choice(self):

        choose = input("Press 'b' to Return to main menu or 'e' for Exit")

        if choose == "b":
            self.print_menu()
        elif choose == "e":
            exit()
        else:
            self.intermediate_choice()  # is it even legal? )


class WorkWithFile:
    def save_to_file(self):
        pass

    def load_from_file(self):
        pass


tst_product = Product(125, "Ball", "54621312", "Sport equip")
storage = Storage()
menu = MainMenu()


def main():
    while True:
        menu.print_menu()

        menu_call = float(input("Enter menu #:"))
        if menu_call == 1:
            storage.add_item_manually()
        elif menu_call == 3:
            storage.sell_product()
        elif menu_call == 4:
            storage.print_income()
        elif menu_call == 2:
            storage.add_product_to_storage()
        elif menu_call == 0:
            exit()


if __name__ == '__main__':
    main()
