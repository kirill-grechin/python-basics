import re
from datetime import datetime


class Date:
    __DATE_PATTERN = re.compile(r'^(?:\d{2}-){2}\d{4}$')

    @staticmethod
    def validate_date(date):
        try:
            if not Date.__DATE_PATTERN.match(date):
                raise ValueError('Invalid date format')
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError as ve:
            print(ve)

    @classmethod
    def parse_date_units(cls, date):
        cls.validate_date(date)
        day, month, year = date.split('-')
        return int(day), int(month), int(year)

    def __init__(self, date):
        self.validate_date(date)
        self.__date = date

    @property
    def date(self):
        return self.__date


date = Date('30-05-2020')
print(date.date)
print(Date.parse_date_units('24-05-2007'))
Date.validate_date('45-45-2045')
