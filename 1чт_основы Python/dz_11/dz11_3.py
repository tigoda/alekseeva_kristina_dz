import re


class NotNumber(ValueError):
    pass


answer = None
number_list = []

while NotNumber != 'stop':
    answer = input('Введите число: ')
    if answer == 'stop':
        print(number_list)
        break
    try:
        if not re.match('[-+]?\d+$', answer):
            raise NotNumber("Введенное значение не является числом")
    except NotNumber as err:
        print(err)
    else:
        number_list.append(answer)
        print(f'{number_list}')
