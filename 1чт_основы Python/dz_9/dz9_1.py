import time


class TrafficLight:
    __trafficLight_color = ['red', 'yellow', 'green']

    def running(self):
        for number, color in enumerate(self.__trafficLight_color, 1):
            if number == 1:
                print(color)
                time.sleep(7)
            elif number == 2:
                print(color)
                time.sleep(2)
            elif number == 3:
                print(color)
                time.sleep(5)


a = TrafficLight()
a.running()
