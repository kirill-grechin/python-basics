import urllib.request

"""
1. Не используя библиотеки для парсинга, распарсить файл логов web-сервера nginx_logs.txt.
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
2. * Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов.
код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

log_list, address_dict, response = [], {}, urllib.request.urlopen(URL)
with open('nginx_logs.txt', 'w+', encoding='utf-8') as nginx_logs:
    for line in response:
        nginx_logs.write(line.decode('utf-8'))
    nginx_logs.seek(0)
    for line in nginx_logs:
        split_line = line.replace('"', ' ').replace('-', ' ').split()
        log_list.append((split_line[0], split_line[3], split_line[4]))
        address_dict.setdefault(split_line[0], 0)
        address_dict[split_line[0]] += 1

spammer = max(address_dict, key=address_dict.get)
print(*log_list, f'spammer: {spammer}, spam_count: {address_dict[spammer]}', sep='\n')
