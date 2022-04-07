import json
import os

"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0).
5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>,
[<files_extensions_list>]).
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили
скрипт.
"""

max_length = len(str(max(item.stat().st_size for item in os.scandir('some_data'))))
dictionary = {10 ** length if length != 0 else 0: (0, []) for length in range(max_length + 1)}
for item in os.scandir('some_data'):
    for limit in dictionary:
        if item.stat().st_size < limit:
            count, extens = dictionary[limit]
            extension = item.name.split('.')[1]
            if extension not in set(extens):
                extens.append(extension)
            dictionary[limit] = (count + 1, extens)
            break
with open('summary.json', 'w', encoding='utf-8') as summary:
    json.dump(dictionary, summary, indent=3)
