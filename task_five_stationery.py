from turtle import Screen, Turtle


class Stationery:
    _title = str()

    def _set_turtle(self, color, pensize=1):
        turtle = Turtle()
        turtle.color(color)
        turtle.pensize(pensize)
        turtle.forward(300)
        turtle.left(90)

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def __init__(self):
        self._title = "Ручка"

    def draw(self):
        print(f"Рисует {self._title}.")
        self._set_turtle('blue')
        Screen().resetscreen()


class Pencil(Stationery):

    def __init__(self):
        self._title = "Карандаш"

    def draw(self):
        print(f"Рисует {self._title}.")
        self._set_turtle('grey')
        Screen().resetscreen()


class Handle(Stationery):

    def __init__(self):
        self._title = "Маркер"

    def draw(self):
        print(f"Рисует {self._title}.")
        self._set_turtle('red', 10)
        Screen().exitonclick()


Stationery().draw()

Pen().draw()
Pencil().draw()
Handle().draw()
