from requests import get
from xml.etree import ElementTree
from datetime import datetime
from time import perf_counter
from decimal import Decimal, getcontext

getcontext().prec = 4

# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

# 3. * (вместо 2) Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


# Используя xml.etree
def currency_rates_adv(val):
    root = ElementTree.fromstring(get(API_URL).content)
    for item in root.findall('Valute'):
        if item.find('CharCode').text == val.upper():
            value = Decimal(item.find('Value').text.replace(',', '.'))
            date = datetime.strptime(root.attrib.get('Date'), '%d.%m.%Y').date()
            return {'date': date, 'value': value}


start = perf_counter()
for valute in ('USD', 'EUR', 'GBP', 'chf', 'qwe'):
    val_conv = currency_rates_adv(valute)
    print(f'date: {val_conv.get("date")} value: {val_conv.get("value")}') if val_conv else print(val_conv)
print(perf_counter() - start)


# Используя только методы класса str
def currency_rates(val):
    response = get(API_URL).text
    for char in ('/', '<', '>', '"', '=', '?'):
        response = response.replace(char, ' ')
    res_lst = response.split()
    try:
        val_idx = res_lst.index(val.upper())
        val_idx = res_lst[val_idx:].index('Value') + val_idx + 1
        date_idx = res_lst.index('Date') + 1
    except ValueError:
        return
    value = Decimal(res_lst[val_idx].replace(',', '.'))
    date = datetime.strptime(res_lst[date_idx], '%d.%m.%Y').date()
    return {'date': date, 'value': value}


start = perf_counter()
for valute in ('USD', 'EUR', 'GBP', 'chf', 'qwe'):
    val_conv = currency_rates(valute)
    print(f'date: {val_conv.get("date")} value: {val_conv.get("value")}') if val_conv else print(val_conv)
print(perf_counter() - start)

# По времени методы работают плюс минус одинаково
