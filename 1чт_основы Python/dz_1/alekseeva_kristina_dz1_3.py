answer = 0
for answer in range(1, 101):
    number = answer % 10
    if 11 <= answer <= 14 or number == 0 or 5 <= number <= 9 or 5 <= answer <= 9:
        print(f'{answer} процентов')
    elif number == 1 or answer == 1:
        print(f'{answer} процент')
    elif 2 <= number <= 4 or 2 <= answer <= 4:
        print(f'{answer} процентa')
