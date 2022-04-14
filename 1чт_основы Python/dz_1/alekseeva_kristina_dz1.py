d = 86400
h = 3600
m = 60
while True:
    duration = int(input('Введите количество секунд: '))
    day = duration // d
    hour = (duration - d * day) // h
    minute = (duration - d * day - h * hour) // m
    second = duration % 60
    if duration < m:
        print(f'{second} сек')
    elif m <= duration < h:
        print(f'{minute} мин {second} сек')
    elif h <= duration < d:
        print(f'{hour} час {minute} мин {second} сек')
    elif duration >= d:
        print(f'{day} дн {hour} час {minute} мин {second} сек')
