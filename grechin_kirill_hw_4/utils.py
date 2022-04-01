from requests import get
from xml.etree import ElementTree
from datetime import datetime
from decimal import Decimal, getcontext

getcontext().prec = 4

API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates_adv(val):
    root = ElementTree.fromstring(get(API_URL).content)
    for item in root.findall('Valute'):
        if item.find('CharCode').text == val.upper():
            value = Decimal(item.find('Value').text.replace(',', '.'))
            date = datetime.strptime(root.attrib.get('Date'), '%d.%m.%Y').date()
            return {'date': date, 'value': value}


if __name__ == '__main__':
    print(currency_rates_adv("USD"))
