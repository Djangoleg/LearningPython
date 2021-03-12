import sys

bakery_file_path = "bakery.csv"


def add_sales(sale):
    program, *args = sale

    if len(args) != 1:
        print("Можно и нужно добавить только одно занчение")
        return

    insert_num = str(args[0]).replace(',', '.')

    if "".join(filter(str.isdigit, insert_num)).isdigit():
        with open(bakery_file_path, 'a', encoding='utf-8') as bakery_sales:
            bakery_sales.write(insert_num + "\n")
    else:
        print("Вводить можно только цифры!")


if __name__ == '__main__':
    add_sales(sys.argv)
