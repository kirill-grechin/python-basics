import sys

"""
7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер 
записи и новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию, 
когда пользователь вводит номер записи, которой не существует. 
"""

if len(sys.argv) == 3:
    with open('bakery.csv', 'r+', encoding='utf-8') as bakery:
        if int(sys.argv[1]) < 1 or int(sys.argv[1]) > bakery.seek(0, 2) // 8:
            print('wrong line number')
            sys.exit(1)
        bakery.seek((int(sys.argv[1]) - 1) * 8)
        for _ in range(1):
            bakery.write(sys.argv[2])
else:
    print('args error')
