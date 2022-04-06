import sys
from itertools import takewhile

"""
7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер
записи и новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию,
когда пользователь вводит номер записи, которой не существует.
"""

if len(sys.argv) == 3:
    with open('bakery.csv', 'r+', encoding='utf-8') as bakery:
        sizes = [len(line) + 1 for index, line in
                 takewhile(lambda x: x[0] < int(sys.argv[1]), enumerate(bakery, start=1))]
        bakery.seek(sum(sizes))
        lines = [f'{sys.argv[2]}\n' if index == 0 else line for index, line in enumerate(bakery)]
        if int(sys.argv[1]) > len(sizes) + len(lines):
            print('wrong row number')
            sys.exit(1)
        bakery.truncate(sum(sizes))
    with open('bakery.csv', 'a', encoding='utf-8') as bakery:
        for line in lines:
            bakery.write(line)
else:
    print('args error')
