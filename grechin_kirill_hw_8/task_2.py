import re
import urllib.request

# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
# урока nginx_logs.txt для получения информации вида: (<remote_addr>, <request_datetime>,
# <request_type>, <requested_resource>, <response_code>, <response_size>).

RE_PATTERN = re.compile(
    r'(?P<address>^\S+)[\s-]*\[(?P<datetime>[^]]+)]\s*\"(?P<request>[A-Z]+)'
    r'\s*(?P<resource>[/\w]+)[^\"]*\"\s*(?P<code>\d+)\s*(?P<size>\d+)')

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

response = urllib.request.urlopen(URL)
parse_list = [RE_PATTERN.findall(line.decode('utf-8'))[0] for line in response]
print(*parse_list, sep='\n')
