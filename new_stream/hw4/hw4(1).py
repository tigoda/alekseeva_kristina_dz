# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import decimal

a = decimal.Decimal(input('введите a '))
b = decimal.Decimal(input('введите b '))
print(f"{a:.{abs(b.as_tuple().exponent)}f}")
