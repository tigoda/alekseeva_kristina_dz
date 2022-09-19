# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input())
list_ = []
simple = 2
while num > 1:
    if num % simple == 0:
        list_.append(simple)
        num = num/simple
    else:
        simple += 1
print(list_)