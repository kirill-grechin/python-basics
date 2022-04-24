class ComplexNumber:
    def __init__(self, number):
        self.__number = number

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return str(self.number)[1:-1]

    def __add__(self, other):
        return ComplexNumber(self.number + other.number)

    def __mul__(self, other):
        return ComplexNumber(self.number * other.number)


number_1 = ComplexNumber(2 + 3j)
number_2 = ComplexNumber(-5 - 6j)
print(number_1 + number_2)
print(number_1 * number_2)
