# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

import numpy as np

# a = np.poly1d([r.randint(0, 100) for _ in range(int(input('введите степень :')))])
print(np.poly1d([random.randint(0, 100) for _ in range(int(input('введите степень :')))]))
