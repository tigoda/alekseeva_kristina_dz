class ComplexNumber:

    def __init__(self, number1, number2):
        self.numbers = complex(number1, number2)

    def __str__(self):
        return f'{self.numbers}'

    def __add__(self, other):
        return ComplexNumber(self.numbers + other.numbers, 0)

    def __mul__(self, other):
        return ComplexNumber(self.numbers * other.numbers, 0)


a = ComplexNumber(10, 11)
b = ComplexNumber(-20, 5)
print(a, b)
print(a + b)
print(a * b)
