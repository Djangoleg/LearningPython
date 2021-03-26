class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        pass

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        sub = self.cell - other.cell
        if sub > 0:
            return sub
        else:
            return "Вычитание невозможно!"

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        if other.cell == 0:
            return self.cell
        else:
            return self.cell // other.cell

    def __truediv__(self, other):
        if other.cell == 0:
            return self.cell
        else:
            return int(round(self.cell / other.cell, 0))

    def make_order(self, rows):
        f_str = str()
        for idx, _ in enumerate(range(self.cell), 1):
            f_str += "* "
            if idx % rows == 0:
                f_str += "\n"

        return f_str


cell_1 = Cell(9)
cell_2 = Cell(11)
print(cell_1 + cell_2)
print(cell_2.make_order(4))
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1 / cell_2)
