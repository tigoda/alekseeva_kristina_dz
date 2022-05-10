class Cell:

    def __init__(self, amount):
        self.amount = amount

    def make_order(self, cells):
        order = ''
        for _ in range(self.amount // cells):
            order += '*' * cells + '\n'
        order += '*' * (self.amount % cells)
        return order

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        result = self.amount - other.amount
        if result > 0:
            return Cell(self.amount - other.amount)
        else:
            raise ValueError('Результат не может быть отрицательным')

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __floordiv__(self, other):
        return Cell(self.amount // other.amount)


cell_1 = Cell(20)
print(cell_1.make_order(3))

cell_2 = Cell(7)
a = cell_1 + cell_2
print(a.make_order(7))

b = cell_1 - cell_2
print(b.make_order(10))

# c = cell_2 - cell_1
# print(c.make_order(4))

d = cell_1 * cell_2
print(d.make_order(15))

e = cell_1 // cell_2
print(e.make_order(7))
