with open("users.csv", 'r', encoding='utf-8') as users:
    with open("hobby.csv", 'r', encoding='utf-8') as hobbys:
        with open('users_hobby.txt', 'w', encoding='utf-8') as users_hobby:
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
