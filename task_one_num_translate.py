translate_dict = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}


def num_translate_adv(key):
    if key == key.title():
        return translate_dict.get(key).title()
    return translate_dict.get(key.lower())


# Проверка с маленькой буквы.
for k in translate_dict:
    print(num_translate_adv(k))

print("*" * 20)

# Проверка с заглавной буквы.
for k in translate_dict:
    print(num_translate_adv(k).title())

print("*" * 20)

# Вывод None.
print(num_translate_adv("eleven"))
