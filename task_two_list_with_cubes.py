list_cubes = list()
for x in range(1000):
    if x % 2 != 0:
        list_cubes.append(x ** 3)

# Список нечетных кубов.
print(list_cubes)

list_sum_number = list()

# Поиск элементов списка у которых сумма цифр делется на 7 без остатка.
for numb in list_cubes:
    memo_numb = numb
    sum_number = 0
    while numb:
        sum_number += numb % 10
        numb //= 10
    if sum_number % 7 == 0:
        list_sum_number.append(memo_numb)

# Список элементов у которых сумма цифр делется на 7 без остатка.
print(list_sum_number)

# Инкремент на 17, элементов списка с кубами list_cubes.
print([x + 17 for x in list_cubes])

list_sum_number.clear()

# Поиск элементов списка у которых сумма цифр делется на 7 без остатка.
for numb in [x + 17 for x in list_cubes]:
    memo_numb = numb
    sum_number = 0
    while numb:
        sum_number += numb % 10
        numb //= 10
    if sum_number % 7 == 0:
        list_sum_number.append(memo_numb)

print(list_sum_number)
