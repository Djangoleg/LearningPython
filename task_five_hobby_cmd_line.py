import os.path


def create_users_hobby(argv):
    program, *args = argv

    # Проверка на количество переданных аргументов.
    if len(args) != 3:
        print("Нужно передать 3 пути к файлам. 1 - путь и имя файла с пользователями(users.csv), "
              "2 - путь и имя файла с хобби(hobby.csv), 3 - путь и имя файла(users_hobby.txt), "
              "который объединит первые два.")
        return

    # Проверка на существование файлов.
    if not os.path.isfile(args[0]):
        print(f"{args[0]} - файл не существует!")
        return

    if not os.path.isfile(args[0]):
        print(f"{args[1]} - файл не существует!")
        return

    with open(args[0], 'r', encoding='utf-8') as users:
        with open(args[1], 'r', encoding='utf-8') as hobbys:
            with open(args[2], 'w', encoding='utf-8') as users_hobby:
                users_raw_line = users.readline()
                hobbys_raw_line = hobbys.readline()
                while users_raw_line or hobbys_raw_line:
                    users_line = " ".join(users_raw_line.split(",")).rstrip()
                    hobbys_line = " ".join(hobbys_raw_line.split(" ")).rstrip()

                    if not users_line:
                        users_line = str(None)
                    if not hobbys_line:
                        hobbys_line = str(None)

                    users_hobby.writelines(f'{users_line}: {hobbys_line}\n')
                    # print(f'{users_line}: {hobbys_line}')
                    users_raw_line = users.readline()
                    hobbys_raw_line = hobbys.readline()

    print(f"Создан объединённый файл {os.path.abspath(args[2])}.")


if __name__ == '__main__':
    import sys

    create_users_hobby(sys.argv)
