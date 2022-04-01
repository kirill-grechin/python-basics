# 3. * Решить задачу 2, не создавая новый список.

str_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов,',
            'а', 'в', '9', 'часов', '7', 'минут', 'температура', 'воздуха', 'была', '-9', 'градусов']

out_line, index = '', 0

while index < len(str_list):
    item = str_list[index]
    if item.isdigit():
        str_list[index:index + 1] = ('"', f'{int(item):02}', '"')
        item, index = ''.join(str_list[index:index + 3]), index + 2
    elif item[0] in ('+', '-') and item[1:].isdigit():
        str_list[index:index + 1] = ('"', f'{item[0]}{int(item[1:]):02}', '"')
        item, index = ''.join(str_list[index:index + 3]), index + 2
    out_line, index = f'{out_line} {item}', index + 1

print(str_list, out_line.lstrip(), sep='\n')
