class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if not is_police:
            print(f'скорость: {speed}км, цвет: {color}, название: {name}')
        else:
            print(f'{speed},{color},{name} - полицейская машина')

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} превышена на {self.speed - 60} км')
        else:
            print(f'Скорость {self.name} составляет {self.speed}')


class SportCar(Car):
    def sport_car_speeed(self):
        print(f'Скорость {self.name} составляет {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} превышена на {self.speed - 40} км')
        else:
            print(f'Скорость {self.name} составляет {self.speed}')


class PoliceCar(Car):
    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed}')


a = Car(200, 'красный', 'Мазда')
a.go()
a.stop()
a.turn('на лево')
a.show_speed()
b = TownCar(250, 'зеленый', 'Мазда')
b.go()
b.stop()
b.turn('на право')
b.show_speed()
c = WorkCar(70, 'белый', 'Мазда')
c.go()
c.stop()
c.turn('назад')
c.show_speed()
d = PoliceCar(547, 'желтый', 'Мазда', True)
d.go()
d.stop()
d.turn('назад')
d.show_speed()
