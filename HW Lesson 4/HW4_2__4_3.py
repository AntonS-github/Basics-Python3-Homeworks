import requests.utils
from datetime import datetime
from decimal import Decimal


def currency_rates(*cur_request):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encoded_resp = requests.utils.get_encoding_from_headers(response.headers)
    full_content = response.content.decode(encoding=encoded_resp)
    full_content = full_content.split('</')
    cur_names_list = []
    cur_values_list = []
    list_of_results = []
    for el in full_content:
        list_of_str = el
        list_of_str = list_of_str.split('>')
        for cur_name in list_of_str:
            if cur_name.isupper():
                cur_names_list.append(cur_name)
        value = cur_name.replace(',', '.')  # делаем float
        value = value.lower()
        if value.isdigit() == False and value.islower() == False and value != '':
            cur_values_list.append(Decimal(value).quantize(Decimal('1.00')))  # сразу переделываем в decimal
    cur_dict = dict(zip(cur_names_list, cur_values_list))
    for i in cur_request:
        i = i.upper()  # делаем отвязку от регистра введёного аргумента
        if i in cur_dict:
            result = f'{i}: {cur_dict[i]}, '
            list_of_results.append(result)
        else:
            list_of_results.append('None')
    return *list_of_results, datetime.now().strftime(", %d.%m.%Y, %H:%M:%S") # вывод даты для задания 3 со звездой
if __name__ == "__main__":
    print(*currency_rates('EUR', 'usd', 'DKK', 'GGG'))  # GGG - проверяем что выдаст на несуществующую валюту

