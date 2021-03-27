class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите число, на которое будет разделено число 100: ")

try:
    inp_data = int(inp_data)
    if inp_data == 0:
        raise MyZeroDivision(f"{inp_data}\nВы ввели {inp_data}. На {inp_data} делить нельзя!")
except ValueError:
    print(f"{inp_data}\nВы ввели не число.")
except MyZeroDivision as err:
    print(err)
else:
    print(f"{inp_data}\nВсе хорошо. Результат: {round(100 / inp_data, 2)}")
