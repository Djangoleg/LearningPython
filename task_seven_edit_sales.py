import os.path
import sys

bakery_file_path = "bakery.csv"
bakery_file_path_temp1 = "tmp_bakery_1.csv"
bakery_file_path_temp2 = "tmp_bakery_2.csv"


def edit_sales(argv):
    """
    Не получилось использовать то красивое решение,
    что было на объяснении ДЗ. Почему-то оно у меня не работает.
    Забить пробелами можно большую строку, но что делать, если вводить
    строку больше чем, была введена ранее? Она перезапишет данные,
    которые не при чем. Тут не угадаешь.
    Раз нельзя перегружать оперативу, будем использовать HDD. Надеюсь по
    заданию его полно.
    :param argv:
    :return:
    """
    program, *args = argv

    if not os.path.isfile(bakery_file_path):
        print("Данные отсутствуют")
    else:
        if 2 > len(args) > 2:
            print("Функция принимает только 2-а аргумента")
            return

        # Проверки на введенные цифры.
        pos, val = str(args[0]), str(args[1]).replace(',', '.')

        if not "".join(filter(str.isdigit, pos)).isdigit() and "".join(filter(str.isdigit, val)).isdigit():
            print("Вводить можно только цифры!")
            return

        pos, val = int(pos), float(val)

        # Разделение на 2 временных файла.
        with open(bakery_file_path, 'r', encoding="utf-8") as bakery_file:

            # Тяжелая проверка вопреки.
            line_count = sum(1 for line in bakery_file)
            if pos < 0 or pos > line_count:
                print("Переданное значение номера строки в файле отсутствует!")
                return

            # Возврат курсора.
            bakery_file.seek(0)

            with open(bakery_file_path_temp1, 'w', encoding="utf-8") as tmp_bakery_1:
                with open(bakery_file_path_temp2, 'w', encoding="utf-8") as tmp_bakery_2:

                    for idx, line in enumerate(bakery_file, 1):
                        if idx < pos:
                            tmp_bakery_1.writelines(line)
                        elif idx > pos:
                            tmp_bakery_2.writelines(line)

        # Первая часть. Записываем то что было до pos.
        with open(bakery_file_path_temp1, 'r', encoding="utf-8") as tmp_bakery_1:
            with open(bakery_file_path, 'w', encoding="utf-8") as bakery_file:
                for line in tmp_bakery_1:
                    bakery_file.writelines(line)

        # Вторая часть. Записываем новое значение и то что было после pos.
        with open(bakery_file_path_temp2, 'r', encoding="utf-8") as tmp_bakery_2:
            with open(bakery_file_path, 'a', encoding="utf-8") as bakery_file:
                # Новое значение.
                bakery_file.writelines(str(val) + "\n")
                # Остаток.
                for line in tmp_bakery_2:
                    bakery_file.writelines(line)

        # Удаление временных файлов.
        os.remove(bakery_file_path_temp1)
        os.remove(bakery_file_path_temp2)


if __name__ == '__main__':
    edit_sales(sys.argv)
