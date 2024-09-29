class Vehicle:
    __COLOR_VARIANTS = ['red', 'green', 'pink', 'blue', 'black', 'white', 'scarlet']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):

        self.__model = model
        self.__color = color

        self.__engine_power = engine_power
        self.owner = owner
    def get_model(self):
        return self.__model
    def get_horsepower(self):
        return self.__engine_power
    def get_color(self):
        return self.__color
    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    def print_info(self):
        print("Модель:", self.get_model())
        print("Мощность:", self.get_horsepower())
        print("Цвет:", self.get_color())
        print("Владелец:", self.owner)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Сатору Годжо', 'Honda Odissey', 'pink', 1)
vehicle1.print_info()
vehicle1.set_color('Orange')
vehicle1.set_color('green')
vehicle1.owner = 'Джотаро Куджо'
vehicle1.print_info()