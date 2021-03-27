class Warehouse:
    equipment = {}

    def __init__(self, org, org_unit):
        self.org = org
        self.org_unit = org_unit

    def __str__(self):
        f_str = str()
        for k, v in self.equipment.items():
            f_str += f"{k}: "
            for i in v:
                f_str += f"{i}; "
            f_str += "\n"

        return f_str

    def set_equipment(self, equipment):
        """
        Приём оргтехники на склад.
        :param equipment:
        :return:
        """
        equip = equipment.__class__.__name__
        if self.equipment.get(equip):
            self.equipment[equip].append(equipment)
        else:
            self.equipment[equip] = [equipment]

    def get_equipment(self, equipment):
        """
        Передача оргтехники в подразделение.
        :param equipment:
        :return:
        """
        equip = equipment.__class__.__name__
        ou_equipment = dict()
        if self.equipment.get(equip):
            for ind, val in enumerate(self.equipment.get(equip)[:]):
                if equipment == val:
                    result_object = val - equipment
                    if result_object.get_count() == 0:
                        self.equipment.get(equip).pop(ind)
                    else:
                        self.equipment.get(equip)[ind] = result_object

                    ou_equipment[self.org_unit] = equipment

        return ou_equipment


class Equipment:
    __count = int()

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def set_count(self, count):
        if isinstance(count, int):
            self.__count = count
        else:
            raise ValueError(f"Количество оргтехники '{count}' должно быть числом!")

    def get_count(self):
        return self.__count

    def __eq__(self, other):
        return self.name == other.name and self.model == other.model

    def __sub__(self, other):
        sub = self.get_count() - other.get_count()
        if sub > 0:
            self.set_count(sub)
        else:
            self.set_count(0)

        return self


class Printer(Equipment):
    def __init__(self, cartridge_model):
        self.cartridge_type = cartridge_model

    def __str__(self):
        return f"{self.name} {self.model} {self.cartridge_type} {self.get_count()}"


class Scanner(Equipment):
    def __init__(self, scanner_type):
        self.scanner_type = scanner_type

    def __str__(self):
        return f"{self.name} {self.model} {self.scanner_type} {self.get_count()}"


class Copier(Equipment):
    def __init__(self, copier_type):
        self.copier_type = copier_type

    def __str__(self):
        return f"{self.name} {self.model} {self.copier_type} {self.get_count()}"


p1 = Printer(cartridge_model="CF244A")
p1.name = "HP LaserJet Pro M15a"
p1.model = "w2g50a"
p1.set_count(3)

p2 = Printer(cartridge_model="CF300V")
p2.name = "HP LaserJet Pro 1720"
p2.model = "2g50aPro"
p2.set_count(4)

s1 = Scanner(scanner_type="drum")
s1.name = "Fujitsu fi-7260"
s1.model = "4050407"
s1.set_count(2)

s2 = Scanner(scanner_type="flatbed")
s2.name = "HP ScanJet G2410"
s2.model = "10081875"
s2.set_count(2)

c = Copier(copier_type="multi-functional")
c.name = "Xerox B215"
c.model = "B215HJkha"
c.set_count(1)

print("Оргтехника на склад:")
print(p1, p2, s1, s2, c, sep="; ")
print("*" * 20)

# Убираем всю оргтехгику на склад.
w = Warehouse(org="Test_org", org_unit="Test_org_unit")
for x in [p1, p2, s1, s2, c]:
    w.set_equipment(x)
print("Что на складе: ")
print(w)
print("*" * 20)

p4 = Printer(cartridge_model="CF300V")
p4.name = "HP LaserJet Pro 1720"
p4.model = "2g50aPro"
p4.set_count(4)

# Передача принтеров p4 со склада в подразделение Test_org_unit_2
w.org_unit = "Test_org_unit_2"
print("Передача всех принтеров p4 со склада в подразделение Test_org_unit_2: ")
get_p4 = w.get_equipment(p4)
for k, v in get_p4.items():
    print(f"{k}: {str(v)};")
print("*" * 20)
# Остатки на складе:
print("Остатки на складе: ")
print(w)
print("*" * 30)

p3 = Printer(cartridge_model="CF244A")
p3.name = "HP LaserJet Pro M15a"
p3.model = "w2g50a"
p3.set_count(2)

# Передача принтеров p3 со склада в подразделение Test_org_unit_3 - 2 шт.
w.org_unit = "Test_org_unit_3"
print("Передача принтеров p3 со склада в подразделение Test_org_unit_3 - 2 шт.")
get_p3 = w.get_equipment(p3)
for k, v in get_p3.items():
    print(f"{k}: {str(v)};")
print("*" * 30)
# Остатки на складе:
print("Остатки на складе: ")
print(w)
