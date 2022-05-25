class Division_error(ZeroDivisionError):
    pass


number1 = input("Введите  первое значение: ")
number2 = input("Введите  второе значение: ")

try:
    number1 = int(number1)
    number2 = int(number2)
    if number2 == 0:
        raise Division_error("На ноль делить нельзя")
except ValueError:
    print("Вы не верно ввели не число")
except Division_error as err:
    print(err)
else:
    print(f'{number1 / number2}')
