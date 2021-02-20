# Исходный лист.
positions_list = ["инженер-конструктор Игорь", "главный бухгалтер МАРИНА", "токарь высшего разряда нИКОЛАй",
                  "директор аэлита"]

# Приведение  к корректному виду, не создавая новый список.
for idx, item in enumerate(positions_list[:]):
    positions_list[idx] = ["".join(item.split()[-1]).capitalize(),
                           " ".join(item.split()[0:len(item.split()) - 1]).capitalize()]

print(positions_list)

# Фразы вида: Привет, Игорь!
for name in positions_list:
    print(f"Привет, {name[0]}!")
