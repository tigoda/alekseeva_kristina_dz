def num(translate):
    words = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
             'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return words.get(translate)


while True:
    answer = input('Введите число: ')
    print(num(answer))
