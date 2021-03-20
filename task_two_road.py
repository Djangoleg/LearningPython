class Road:
    __length = 0
    __width = 0

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_weight(self):
        m = (self.__length * self.__width * 25 * 5) / 1000
        return round(m, 2)


r = Road(20, 5000)
print(f"Необходимо {r.calc_weight()} тонн")
