prises_list = [0.04, 80.5, 234.06, 10.05, 160.5, 49.5, 13.68, 182.07, 183.67, 143.65, 10.51, 87, 45.91, 63.95, 298.93,
               265.64, 36.75, 356.69, 370.5, 46.3, 231.98, 221.16, 21.2, 4382.91, 27661.5, 33, 49.06, 12264.23, 1438.47,
               32.9]

# 1. Цены через запятую в одну строку
for price in prises_list:
    print(f"{int(price):02} руб {int((price - int(price)) * 100):02} коп", end=", ")

print("\n", id(prises_list))

print("\n\n", "*" * 30)
#  ----------Как было нужно отделить копейки---------------------------
for i in prises_list:
    rub, kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {int(kop):02d} коп", end=" ")
#  --------------------------------------------------------------------
print("\n\n", "*" * 30)


# 2. Цены, отсортированные по возрастанию, новый список не создавать.
prises_list.sort()

print(prises_list)

print("\n")
print(id(prises_list))

# 3. Новый список, содержащий те же цены, но отсортированные по убыванию.
prises_list_new = sorted(prises_list, reverse=True)

print(prises_list_new)

# Список новый.
print(id(prises_list_new))

# 4. Вывести цены пяти самых дорогих товаров.
print(prises_list_new[:5:1])

# 4.1. Вывести цены этих товаров по возрастанию, написав минимум кода
print(sorted(prises_list_new[:5:1], reverse=False))
