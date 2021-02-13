class Road:
    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width

    def calculate_weight(self, square_meter: int, depth: int):
        return self.__width * self.__length * square_meter * depth


road = Road(100, 100)
road.calculate_weight(1, 10)
