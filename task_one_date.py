import datetime


class Date:
    def __init__(self, date):
        Date.date = date

    @classmethod
    def get_number_for_date(cls):
        try:
            date_time = datetime.datetime.strptime(cls.date, "%d.%m.%Y")
        except ValueError as e:
            print(f"ValueError: {e}")
        else:
            return [date_time.day, date_time.month, date_time.year]

    @staticmethod
    def check_date(day, month, year):
        if not 1 <= day <= 31:
            print(f"Номер дня '{day}' должен быть в интервале от 1..31")
            return False
        if not 1 <= month <= 12:
            print(f"Номер месяца '{month}' должен быть в интервале от 1..12")
            return False
        if not 1 <= year <= 9999:
            print(f"Год '{year}' должен быть в интервале от 1..9999")
            return False

        return True


date = Date("27.03.2021")
dmy = date.get_number_for_date()
if dmy:
    print(dmy)
    print(date.check_date(*dmy))

print(date.check_date(27, 3, 10000))

