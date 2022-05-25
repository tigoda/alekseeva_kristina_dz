import numpy as np


class Matrix:
    def __init__(self, *args: list):
        self.args = np.array(args)

    def __str__(self):
        return "{}".format(f'{str(self.args).replace("[", "|").replace("]", "|")}  \n')

    def __add__(self, other):
        return Matrix(self.args + other.args)


a = Matrix([1, 2], [3, 4], [5, 6])
b = Matrix([7, 8], [9, 10], [11, 12])
print(a, b, a + b)
