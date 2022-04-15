import re

# Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
# виде словаря. Если адрес не валиден, выбросить исключение ValueError.

RE_EMAIL = re.compile(r'^[a-z][a-z0-9._]*[a-z0-9]@[a-z]+\.[a-z]+$')


def email_parse(email):
    if not RE_EMAIL.match(email):
        raise ValueError(f'wrong email "{email}')
    username, domain = email.split('@')
    if not check_dots_and_underscores(username):
        raise ValueError(f'wrong email "{email}')
    return {'username': username, "domain": domain}


def check_dots_and_underscores(username):
    if username.count('_') == 0 and username.count('.') == 0:
        return True
    for index in range(len(username) - 1):
        if username[index] in ('_', '.') and username[index + 1] in ('_', '.'):
            return False
    return True


try:
    print(email_parse('ivan_ivanov01@mail.ru'))
    print(email_parse('i.v.a.n.o.v01@mail.ru'))
    print(email_parse('i__v.a.n.o.v@mail.ru'))
except ValueError as ve:
    print(ve)
