class Road:

    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width

    def get_mass(self):
        return int((self.__length * self.__width * 25 * 5) / 1000)


road = Road(20, 5000)
print(road.get_mass())
