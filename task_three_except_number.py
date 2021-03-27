class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите число: ")
print(inp_data, sep="\n")
num_list = list()

while inp_data.lower() != "stop" and inp_data.lower() != "exit":
    try:
        if inp_data.isdigit():
            num_list.append(int(inp_data))
        else:
            raise NotNumber(f"\nВы ввели - '{inp_data}'. Это не число!")

        inp_data = input("Введите число: ")
        print(inp_data, sep="\n")

    except NotNumber as err:
        print(err)
        inp_data = input("Введите число: ")
        print(inp_data, sep="\n")

print(f"\nВы вводили: {', '.join(str(n) for n in num_list)}")
