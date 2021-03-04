from datetime import datetime
from decimal import Decimal
from requests import get, utils

val_server_url = "http://www.cbr.ru/scripts/XML_daily.asp"


def currency_rates(argv):
    program, *args = argv
    val_dict = {}
    summary_list = []

    # Get server data.
    response = get(val_server_url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = str(response.content.decode(encoding=encodings))

    # Hard coding.
    date_str = content.split('<ValCurs')[1].split('name="Foreign Currency Market">')[0].split('Date="')[1].split('"')[0]
    val_dict["date"] = datetime.strptime(date_str, '%m.%d.%Y')

    tmp_list = content.split('<Valute')[1::]

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


if __name__ == '__main__':
    import sys

    print(currency_rates(sys.argv))
