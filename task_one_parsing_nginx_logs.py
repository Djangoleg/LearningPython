final_list = list()
with open("nginx_logs.txt", 'r', encoding='utf-8') as nginx_logs:
    for line in nginx_logs:
        remote_addr = line[0:][:line.index(" - - ")]
        camel_case_index = line.index("\"") + 1
        method_type_and_request_row = line[camel_case_index:][:line[camel_case_index:].index("\"")].split(" ")
        request_type = method_type_and_request_row[0]
        requested_resource = method_type_and_request_row[1]
        final_list.append((remote_addr, request_type, requested_resource))

# Поиск спамера.
spammers = dict()
for i in final_list:
    spammers[i[0]] = spammers.get(i[0], 0) + 1

max_spammer_key = max(spammers, key=spammers.get)
print(f"Max number of connections from IP: {max_spammer_key}. "
      f"Number of connections: {spammers[max_spammer_key]}")

print("*" * 20)
# Дополнительная проверка. Выведем тех, кто подключался больше 1000 раз.
for key in sorted(spammers, key=spammers.get, reverse=True):
    if spammers[key] > 1000:
        print(key, spammers[key])
