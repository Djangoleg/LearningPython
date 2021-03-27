class Warehouse:
    equipment = []

    def __init__(self, org, org_unit, equipment):
        self.org = org
        self.org_unit = org_unit
        self.equipment = equipment

    def __str__(self):
        return "".join(str(n) for n in self.equipment)


class Equipment:
    def __init__(self, name, model, sn):
        self.name = name
        self.model = model
        self.sn = sn


class Printer(Equipment):
    def __init__(self, cartridge_model):
        self.cartridge_type = cartridge_model

    def __str__(self):
        return f"{self.name} {self.model} {self.sn} {self.cartridge_type};\n"


class Scanner(Equipment):
    def __init__(self, scanner_type):
        self.scanner_type = scanner_type

    def __str__(self):
        return f"{self.name} {self.model} {self.sn} {self.scanner_type};\n"


class Copier(Equipment):
    def __init__(self, copier_type):
        self.copier_type = copier_type

    def __str__(self):
        return f"{self.name} {self.model} {self.sn} {self.copier_type};\n"


p = Printer(cartridge_model="CF244A")
p.name = "HP LaserJet Pro M15a"
p.model = "w2g50a"
p.sn = "001-00001"

s = Scanner(scanner_type="flatbed")
s.name = "HP ScanJet G2410"
s.model = "10081875"
s.sn = "001-00002"

c = Copier(copier_type="multi-functional")
c.name = "Xerox B215"
c.model = "B215HJkha"
c.sn = "001-00003"

print(p, s, c, sep="")

# Убираем на склад.
w = Warehouse(org="Test_org", org_unit="Test_unit", equipment=[p, s, c])
print("На складе:\n", w, sep="")
