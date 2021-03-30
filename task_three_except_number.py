class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


def try_parse_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def try_parse_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


inp_data = input("Введите число: ")
print(inp_data, sep="\n")
num_list = list()

while inp_data.lower() != "stop" and inp_data.lower() != "exit":
    try:
        if try_parse_int(inp_data):
            num_list.append(int(inp_data))

        elif try_parse_float(inp_data):
            num_list.append(float(inp_data))
        else:
            raise NotNumber(f"\nВы ввели - '{inp_data}'. Это не число!")

        inp_data = input("Введите число: ")
        print(inp_data, sep="\n")

    except NotNumber as err:
        print(err)
        inp_data = input("Введите число: ")
        print(inp_data, sep="\n")

print(f"\nВы вводили: {', '.join(str(n) for n in num_list)}")
