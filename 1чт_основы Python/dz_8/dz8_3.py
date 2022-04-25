def type_logger(func):
    def wrapper(*args):
        args_data = []
        for el in args:
            args_data.append(f' {el} : {type(el)}')
        print(args_data)
        return func(*args)

    return wrapper


@type_logger
def calc_cube(x, y):
    return x ** 3, y ** 5


a = calc_cube(5, 7)

print(a)
