final_list = list()
with open("nginx_logs.txt", 'r', encoding='utf-8') as nginx_logs:
    for line in nginx_logs:
        remote_addr = line[0:][:line.index(" - - ")]
        camel_case_index = line.index("\"") + 1
        method_type_and_request_row = line[camel_case_index:][:line[camel_case_index:].index("\"")].split(" ")
        request_type = method_type_and_request_row[0]
        requested_resource = method_type_and_request_row[1]
        final_list.append((remote_addr, request_type, requested_resource))

# print(*final_list, sep="\n")
# Поиск спамера.
spamers = dict()
for i in final_list:
  spamers[i[0]] = spamers.get(i[0], 0) + 1

# Сортировка по максимальному количеству коннектов. Order by Descending for Value.
print(dict(sorted(spamers.items(), key=lambda item: item[1], reverse=True)))



