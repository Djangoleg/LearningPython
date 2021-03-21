import random


class Car:
    speed = 0
    color = str()
    name = str()
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self):
        self.speed = random.randrange(10, 150)
        print("Машина поехала!")

    def stop(self):
        self.speed = 0
        print("Машина остановилась!")

    def turn(self, direction):
        if self.speed == 0:
            print(f"Машина стоит на месте!")
        else:
            print(f"Машина повернула {direction}!")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed}!")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость автомобиля превышена {self.speed}!")
        else:
            print(f"Скорость автомобиля {self.speed}!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость автомобиля превышена {self.speed}!")
        else:
            print(f"Скорость автомобиля {self.speed}!")


class SportCar(Car):
    def go(self):
        self.speed = random.randrange(150, 450)
        print("Машина поехала!")


class PoliceCar(Car):
    __siren_on = False

    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True

    def siren_on(self):
        self.__siren_on = True
        print("Сирена включена!")

    def siren_off(self):
        self.__siren_on = False
        print("Сирена выключена!")

    def get_siren_status(self):
        if self.__siren_on:
            print("Сирена включена!")
        else:
            print("Сирена выключена!")

        return self.__siren_on


print("Car " + ("*" * 40))
# Test Car class
c = Car("Red", "Mazda")
c.show_speed()
c.go()
c.show_speed()
c.turn("влево")
c.turn("вправо")
c.stop()
c.show_speed()

print("TownCar " + ("*" * 40))
# Test TownCar
t = TownCar("Black", "Renault Twingo")
t.show_speed()
t.go()
t.turn("влево")
t.turn("вправо")
t.show_speed()
t.stop()
t.show_speed()
t.turn("влево")

print("WorkCar " + ("*" * 40))
# Test WorkCar
w = WorkCar("Green", "Caterpillar")
w.show_speed()
w.go()
w.turn("влево")
w.turn("вправо")
w.show_speed()
w.stop()
w.show_speed()
w.turn("влево")

print("SportCar " + ("*" * 40))
# Test SportCar
s = SportCar("Blue", "Bugatti")
s.show_speed()
s.go()
s.turn("влево")
s.turn("вправо")
s.show_speed()
s.stop()
s.show_speed()
s.turn("влево")

print("PoliceCar " + ("*" * 40))
# Test PoliceCar
p = PoliceCar("black/white", "PoliceCar")
print(f"Это машина полиции? {p.is_police}")

siren_status = p.get_siren_status()
if siren_status:
    p.siren_off()
else:
    p.siren_on()
p.get_siren_status()

p.show_speed()
p.go()
p.turn("влево")
p.turn("вправо")
p.show_speed()
p.stop()
p.show_speed()
p.turn("влево")
