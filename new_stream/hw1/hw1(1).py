# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

y = int(input('Введите число'))
if 6 <= y <= 7:
    print('Это выходной')
else:
    print('Будний')
