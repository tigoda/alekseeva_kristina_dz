var = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for el in var:
    names = ''.join(el.split()[-1]).title()
    print(f'Привет, {names}!')