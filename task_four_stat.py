import os
from collections import defaultdict

# Анализируем папку some_data из задания.
root_dir = "some_data"
data_files = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        data_files[file_size] += 1

for k, v in sorted(data_files.items()):
    print(f"{k}: {v}")


