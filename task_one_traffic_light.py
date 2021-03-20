import time


class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def __signals_change(self):
        print("\033[31m {}".format(self.__color[0]))
        time.sleep(7)
        print("\033[33m {}".format(self.__color[1]))
        time.sleep(2)
        print("\033[32m {}".format(self.__color[2]))
        time.sleep(5)

    def running(self, cycles_number=None):
        if cycles_number:
            count = 0
            while count < cycles_number:
                self.__signals_change()
                count += 1
        else:
            while True:
                self.__signals_change()


t = TrafficLight()
t.running(2)
