import re

# Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
# виде словаря. Если адрес не валиден, выбросить исключение ValueError.

RE_EMAIL = re.compile(r'^[a-z][a-z0-9_]*[a-z0-9]@[a-z]+\.[a-z]+$')


def email_parse(email):
    if RE_EMAIL.match(email):
        return {'username': email.split('@')[0], 'domain': email.split('@')[1]}
    raise ValueError(f'wrong email: "{email}"')


try:
    print(email_parse('ivan_ivanov@mail.ru'))
    print(email_parse('_ivan_ivanov@mail.ru'))
except ValueError as ve:
    print(ve)
