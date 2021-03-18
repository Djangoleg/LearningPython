import os
import django
import json

# Анализируем папку c django из задания.
root_dir = django.__path__[0]
data_files = dict()
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        ext = file.split(".")[1:]
        if len(ext) > 0:
            ext = ext[0]
            if file_size in data_files:
                data_files[file_size][0] += 1
                if ext not in data_files[file_size][1]:
                    data_files[file_size][1].append(ext)
            else:
                data_files[file_size] = [1, [ext]]

# Перегоняем в новый словарь, с кортежами.
final_dict = dict()
for k, v in sorted(data_files.items()):
    final_dict[k] = tuple(v)

# Проверка.
print(*final_dict.items(), sep="\n")

# Сохранение в json.
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "summary.json"), 'w') as f:
    json.dump(final_dict, f)