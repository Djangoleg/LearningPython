from turtle import Screen, Turtle

class Stationery:
    _title = str()

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def __init__(self):
        self._title = "Ручка"

    def draw(self):
        print(f"Рисует {self._title}.")
        turtle = Turtle()
        turtle.color('blue')
        turtle.forward(300)
        turtle.left(90)
        screen = Screen()
        screen.resetscreen()


class Pencil(Stationery):

    def __init__(self):
        self._title = "Карандаш"

    def draw(self):
        print(f"Рисует {self._title}.")
        turtle = Turtle()
        turtle.color('grey')
        turtle.forward(300)
        turtle.left(90)
        screen = Screen()
        screen.resetscreen()


class Handle(Stationery):

    def __init__(self):
        self._title = "Маркер"

    def draw(self):
        print(f"Рисует {self._title}.")
        turtle = Turtle()
        turtle.pensize(10)
        turtle.color('red')
        turtle.forward(300)
        turtle.left(90)
        screen = Screen()
        screen.exitonclick()


Stationery().draw()

Pen().draw()
Pencil().draw()
Handle().draw()
