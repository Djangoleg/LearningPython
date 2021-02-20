# Исходный лист.
str_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Добавить кавычку до и кавычку после элемента списка, являющегося числом.
# И дополнить нулём до двух целочисленных разрядов.
count = 0
for idx, item in enumerate(str_list[:]):
    digit = "".join(filter(str.isdigit, item))
    if digit != "":
        if int(digit) // 10 == 0:
            if str_list[idx + count][0].isdigit():
                str_list[idx + count] = "0" + digit
            else:
                str_list[idx + count] = str_list[idx + count][0] + "0" + digit

        str_list.insert(idx + count, '"')
        str_list.insert(idx + count + 2, '"')
        count += 2

print(str_list)

summary = str()
count_camels = 0

# Формирование из списка строки. Возможно можно проще и красивее.
for idx, item in enumerate(str_list):
    if item != '"':
        if count_camels == 0 and idx < len(str_list) - 1:
            summary += item + " "
        else:
            summary += item
    else:
        count_camels += 1
        summary += item
        if count_camels == 2 and idx < len(str_list) - 1:
            summary += " "
            count_camels = 0

print(summary)
