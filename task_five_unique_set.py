src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_elements = set()
for el in src:
    if el not in unique_elements:
        unique_elements.add(el)
    else:
        unique_elements.discard(el)

# Уникальные элементы.
print(unique_elements)
# Сортировка как в исходном списке.
unique_elements_ord = [el for el in src if el in unique_elements]
print(unique_elements_ord)
