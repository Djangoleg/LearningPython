import os.path
import sys

bakery_file_path = "bakery.csv"


def show_sales(argv):
    program, *args = argv

    if not os.path.isfile(bakery_file_path):
        print("Данные отсутствуют")
    else:
        if not 0 <= len(args) <= 2:
            print("Функция принимает от 0 до 2-х аргументов")
            return

        start, end = -1, -1

        if len(args) == 0:
            start = 0
        elif len(args) > 1:
            start = int(args[0])
            end = int(args[1])
        else:
            start = int(args[0])

        bakery_sales = open(bakery_file_path)

        if end == -1:
            end = sum(1 for line in bakery_sales)
            # Возврат курсора.
            bakery_sales.seek(0)

        for i, line in enumerate(bakery_sales, 1):
            if start <= i <= end:
                print(line, end="")
            elif i >= end:
                break

        bakery_sales.close()


if __name__ == '__main__':
    show_sales(sys.argv)
