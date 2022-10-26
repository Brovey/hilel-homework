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


class Storage:
    def __init__(self, quantity):
        self.quantity = quantity
    pass


class MainMenu:

    pass


class WorkWithFile:
    pass


tst_product = Product(125, "Ball", "54621312", "Sport equip")


def main():
    print("Product balance")
    print("Current income")
    print("Total income")
    print("Save to file")
    print("Load from file")
    print("1. Print product chars")
    print("0. Exit")
    while True:
        menu_call = float(input("Enter menu #:"))
        if menu_call == 1:
            tst_product.print_product()
        elif menu_call == 0:
            exit()


if __name__ == "__main__":

    main()
