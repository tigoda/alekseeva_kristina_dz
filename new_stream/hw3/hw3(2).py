# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_ = [2, 3, 4, 5, 6]
# list_ = [2, 3, 5, 6]
print(len(list_))
answer = []
for _ in list_:
    if len(list_) > 1:
        answer.append(list_[0] * list_[-1])
        list_.pop(0)
        list_.pop(-1)
    if len(list_) == 1:
        answer.append(list_[0] * list_[0])

print(answer)
