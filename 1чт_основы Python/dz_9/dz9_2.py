class Road:
    def __init__(self, road_width, road_length):
        self._road_width = road_width
        self._road_length = road_length

    def asphalt_mass(self):
        asphalt_mass = (self._road_width * self._road_length * 5 * 25) // 1000
        print(f'{asphalt_mass} тон')


a = Road(20, 5000)
a.asphalt_mass()
b = Road(30, 7000)
b.asphalt_mass()
