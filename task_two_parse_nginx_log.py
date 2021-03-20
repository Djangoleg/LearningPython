import re

RE_PATTERN = r'((?:\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)|(?:\b\S+\:\S+\b)) \- \- \[(\d+\S+\s+\+\d+)+\] \"+(\w+) (\/\w+\/\w+) \w+\/\w\.\w\" (\d+) (\d+)'

with open("nginx_logs.txt", 'r', encoding='utf-8') as nginx_logs:
    # Запись проверки парсинга в файл nginx_logs_test.txt.
    with open("nginx_logs_test.txt", 'w', encoding='utf-8') as nginx_logs_test:
        print(*[re.findall(RE_PATTERN, line)[0] for line in nginx_logs], sep="\n", file=nginx_logs_test)
