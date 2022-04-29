class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('ЗАПУСК ОТРИСОВКИ')


class Pen(Stationery):
    def draw(self):
        print(f'написать письмо с помощью {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'внести изменения с помощью {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'нарисовать рисунок с помощью {self.title}')


a = Pen('Гелевая ручка')
a.draw()
b = Pencil('Карандаш')
b.draw()
c = Handle('Маркер')
c.draw()
