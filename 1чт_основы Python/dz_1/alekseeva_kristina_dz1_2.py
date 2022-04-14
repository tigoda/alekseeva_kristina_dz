cube = []
suitable_cubes = []
new_cube = []
suitable_new_cubes = []
summer_numbers = 0
summer_numbers_new = 0
for el in range(1, 1001):
    number = el % 2
    if number != 0:
        cube.append(el ** 3)
for num in cube:
    summer_number = 0
    t_num = num
    while num > 0:
        digit_number = num % 10
        if digit_number != 0:
            summer_number += digit_number
        num = num // 10
    if summer_number % 7 == 0:
        suitable_cubes.append(t_num)
for el in suitable_cubes:
    summer_numbers += el
print(summer_numbers)
for el in cube:
    el = el + 17
    new_cube.append(el)
for num in new_cube:
    summer_number_new = 0
    t_num = num
    while num > 0:
        digit_number = num % 10
        if digit_number != 0:
            summer_number_new += digit_number
        num = num // 10
    if summer_number_new % 7 == 0:
        suitable_new_cubes.append(t_num)
for el in suitable_new_cubes:
    summer_numbers_new += el
print(summer_numbers_new)
