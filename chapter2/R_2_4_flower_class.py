__author__ = 'maxiee'

class Flower():
    def __init__(self, name, num_petals, price):
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def set_name(self,name):
        self._name = name

    def set_num_petals(self, num_petals):
        self._num_petals = num_petals

    def set_price(self, price):
        self._price = price

    def get_name(self):
        return self._name

    def get_num_petals(self):
        return self._num_petals

    def get_price(self):
        return self._price

    def print_info(self):
        print("name:", self.get_name())
        print("number of petals:", self.get_num_petals())
        print("price:", self.get_price())

golden_flower = Flower("GoldenFlower", 99, 99999)
golden_flower.print_info()

red_flower = Flower("RedFlower", 5, 2)
red_flower.print_info()

monkey_flower = Flower("MonkeyFlower", 3, 33)
monkey_flower.print_info()