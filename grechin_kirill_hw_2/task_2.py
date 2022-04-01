# 2. Дан список (дополненный):

str_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов,',
            'а', 'в', '9', 'часов', '7', 'минут', 'температура', 'воздуха', 'была', '-9', 'градусов']

# Необходимо его обработать - обособить каждое целое число (вещественные не трогаем) кавычками:
# добавить кавычку до и кавычку после элемента списка, являющегося числом,
# дополнить нулём до двух целочисленных разрядов.

new_str_list = []

for item in str_list:
    if item.isdigit():
        new_str_list.extend(('"', f'{int(item):02}', '"'))
    elif item[0] in ('+', '-') and item[1:].isdigit():
        new_str_list.extend(('"', f'{item[0]}{int(item[1:]):02}', '"'))
    else:
        new_str_list.append(item)

print(new_str_list)

# Сформировать из обработанного списка строку:
# 'в "05" часов "17" минут температура воздуха была "+05" градусов,
# а в "09" часов "07" минут температура воздуха была "-09" градусов'

out_line, index = '', 0

while index < len(new_str_list):
    item = new_str_list[index]
    if item == '"':
        item, index = ''.join(new_str_list[index:index + 3]), index + 2
    out_line, index = f'{out_line} {item}', index + 1

print(out_line.lstrip())
