from datetime import datetime
from decimal import Decimal
from requests import get, utils


def currency_rates(*args):
    val_dict = {}
    summary_list = []

    # Get server data.
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = str(response.content.decode(encoding=encodings))

    # Hard coding.
    tmp_list = content.split('<Valute')
    start_idx = tmp_list[0].index("Date=") + len("Date=") + 1
    end_idx = tmp_list[0][start_idx:].index('"')
    val_dict["date"] = datetime.strptime(tmp_list[0][start_idx:][:end_idx], '%m.%d.%Y')
    tmp_list = tmp_list[1::]

    for row in tmp_list:
        key, value = row.split('<CharCode>')[1].split('</CharCode>')[0], row.split('<Value>')[1].split('</Value>')[0]
        if key and value:
            val_dict[key.lower()] = round(Decimal(value.replace(',', '.')), 2)

    for code in sorted(args):
        code = code.lower()
        if val_dict.get(code):
            summary_list.append(f"{str(code).upper()} : {val_dict.get(code)}, {val_dict.get('date'):%m.%d.%Y}")
        else:
            summary_list.append(f"{str(code).upper()} : {str(val_dict.get(code))}")

    return '\n'.join(summary_list)


# Tests
print(currency_rates("usd", "EUR", "GBP", "BBB", "CHF"))
print("*" * 20)
print(currency_rates("ZAR"))
