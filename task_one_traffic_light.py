import time


class TrafficLight:
    __color = str()

    def __signals_change(self, color, timeout):
        if color == "Red":
            self.__color = "\033[31m {}".format(color)
        elif color == "Yellow":
            self.__color = "\033[33m {}".format(color)
        elif color == "Green":
            self.__color = "\033[32m {}".format(color)
        print(self.__color)
        time.sleep(timeout)

    def running(self, cycles_number=None):
        if cycles_number:
            count = 0
            while count < cycles_number:
                self.__signals_change("Red", 7)
                self.__signals_change("Yellow", 2)
                self.__signals_change("Green", 5)
                count += 1
        else:
            while True:
                self.__signals_change("Red", 7)
                self.__signals_change("Yellow", 2)
                self.__signals_change("Green", 5)


t = TrafficLight()
t.running(2)
