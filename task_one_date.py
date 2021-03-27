import datetime


class Date:
    def __init__(self, date):
        Date.date = date

    @classmethod
    def get_number_for_date(cls):
        date_time = datetime.datetime.strptime(cls.date, "%d.%m.%Y")
        return [date_time.day, date_time.month, date_time.year]

    @staticmethod
    def check_date(day, month, year):
        if not 1 <= day <= 31:
            print(f"Номер дня '{day}' должн быть в интервале от 1..31")
            return False
        if not 1 <= month <= 12:
            print(f"Номер месяца '{year}' должн быть в интервале от 1..12")
            return False
        if not year:
            print(f"Год должен быть инициализирован")
            return False

        return True


date = Date("27.03.2021")
print(date.get_number_for_date())
print(date.check_date(*date.get_number_for_date()))

