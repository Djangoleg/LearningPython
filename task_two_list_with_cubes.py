# Каждый эл-т возводим в куб при добавлении.
list_cubes = list()

for x in range(1, 1001, 2):
    list_cubes.append(x ** 3)

list_sum_number = list()

# Поиск элементов списка у которых сумма цифр делется на 7 без остатка.
for idx, item in enumerate(list_cubes):
    sum_number = 0
    while item:
        sum_number += item % 10
        item //= 10
    if sum_number % 7 == 0:
        list_sum_number.append(list_cubes[idx])

# Сумма элементов.
print("Сумма элементов первого листа:", sum(list_sum_number))

list_sum_number.clear()

# Поиск элементов списка у которых сумма цифр делется на 7 без остатка.
for item in [x + 17 for x in list_cubes]:
    memo_item = item
    sum_number = 0
    while item:
        sum_number += item % 10
        item //= 10
    if sum_number % 7 == 0:
        list_sum_number.append(memo_item)

# Сумма элементов.
print("Сумма элементов второго листа:", sum(list_sum_number))
