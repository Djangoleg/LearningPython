class Worker:
    name = str()
    surname = str()
    position = str()
    _income = dict()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}, {self.position}"

    def get_total_income(self):
        return round(sum(self._income.values()), 2)


p = Position("Иван", "Иванов", "Директор", 200.56, 100.53)
print(p.get_full_name())
print(p.get_total_income())

