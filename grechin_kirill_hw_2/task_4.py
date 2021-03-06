# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:

pos_names_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Известно, что имя сотрудника всегда в конце строки.
# Сформировать из этих имён и вывести на экран фразы вида: 'Привет, Игорь!'.
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

for item in pos_names_list:
    name = item.split()[-1].capitalize()
    print(f'Привет, {name}!')

# Добавил вывод фразы вида: 'Привет, Игорь! Твоя должность: Инженер-конструктор'

for item in pos_names_list:
    split_item = item.split()
    name = split_item[-1].capitalize()
    pos = ' '.join(split_item[:-1]).capitalize()
    print(f'Привет, {name}! Твоя должность: {pos}')
