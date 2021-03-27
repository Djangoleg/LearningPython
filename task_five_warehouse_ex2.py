class Warehouse:
    equipment = {}

    def __init__(self, org, org_unit):
        self.org = org
        self.org_unit = org_unit

    def __str__(self):
        return "".join(f"{k}: {v}; " for k, v in self.equipment.items())

    def set_equipment(self, equipment):
        """
        Приём оргтехники на склад.
        :param equipment:
        :return:
        """
        equip = equipment.__class__.__name__
        if self.equipment.get(equip):
            if isinstance(self.equipment.get(equip), list):
                self.equipment[equip].append(str(equipment))
            else:
                self.equipment[equip] = [self.equipment.get(equip), str(equipment)]
        else:
            self.equipment[equip] = str(equipment)

    def get_equipment(self, equipment):
        """
        Передача оргтехники в подразделение.
        :param equipment:
        :return:
        """
        equip = equipment.__class__.__name__
        ou_equipment = dict()
        if self.equipment.get(equip):
            if isinstance(self.equipment.get(equip), list):
                for ind, val in enumerate(self.equipment.get(equip)[:]):
                    if equipment.sn in val:
                        ou_equipment[self.org_unit] = val
                        self.equipment.get(equip).pop(ind)
            else:
                ou_equipment[self.org_unit] = self.equipment.get(equip)
                del self.equipment[equip]

        return ou_equipment


class Equipment:
    def __init__(self, name, model, sn):
        self.name = name
        self.model = model
        self.sn = sn


class Printer(Equipment):
    def __init__(self, cartridge_model):
        self.cartridge_type = cartridge_model

    def __str__(self):
        return f"{self.name} {self.model} {self.sn} {self.cartridge_type}"


class Scanner(Equipment):
    def __init__(self, scanner_type):
        self.scanner_type = scanner_type

    def __str__(self):
        return f"{self.name} {self.model} {self.sn} {self.scanner_type}"


class Copier(Equipment):
    def __init__(self, copier_type):
        self.copier_type = copier_type

    def __str__(self):
        return f"{self.name} {self.model} {self.sn} {self.copier_type}"


p1 = Printer(cartridge_model="CF244A")
p1.name = "HP LaserJet Pro M15a"
p1.model = "w2g50a"
p1.sn = "001-00001"

p2 = Printer(cartridge_model="CF300V")
p2.name = "HP LaserJet Pro 1720"
p2.model = "2g50aPro"
p2.sn = "001-00004"

s = Scanner(scanner_type="flatbed")
s.name = "HP ScanJet G2410"
s.model = "10081875"
s.sn = "001-00002"

c = Copier(copier_type="multi-functional")
c.name = "Xerox B215"
c.model = "B215HJkha"
c.sn = "001-00003"

print("Оргтехника на склад:")
print(p1, p2, s, c, sep="; ")
print("*" * 20)

# Убираем всю оргтехгику на склад.
w = Warehouse(org="Test_org", org_unit="Test_org_unit")
for x in [p1, p2, s, c]:
    w.set_equipment(x)
print("Что на складе: ")
print(w)
print("*" * 20)

# Передача принтера p2 со склада в подразделение Test_org_unit_2
w.org_unit = "Test_org_unit_2"
print("Передача принтера p2 со склада в подразделение Test_org_unit_2: ")
print(w.get_equipment(p2))
print("*" * 20)
# Остатки на складе:
print("Остатки на складе: ")
print(w)

