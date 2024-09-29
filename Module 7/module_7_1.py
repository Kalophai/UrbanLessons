import os.path

class Product:
    name = ''
    weight = 0
    category = ''

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def add(self, *products):

        products_ = list(products)

        if not os.path.isfile(self.__file_name):
            file = open(self.__file_name, "x")
            file.close()

        with open(self.__file_name, 'r', encoding='utf-8') as file:
            for line in file:
                for item in products:
                    if line == f"{item.name}, {item.weight}, {item.category}\n":
                        print(f"Продукт {item.name} уже есть в магазине")
                        products_.remove(item)
                        break

        if len(products_) > 0:
            file = open(self.__file_name, "a+", encoding='utf-8')
            for item in products_:
                file.write(f"{item.name}, {item.weight}, {item.category}\n")

            file.close()


    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            data = file.readlines()
        return data


def start():
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p1)  # __str__
    print(p2)  # __str__
    print(p3)  # __str__

    s1.add(p1, p2)
    s1.add(p3)

    print(s1.get_products())


if __name__ == '__main__':
    start()