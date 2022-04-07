import json
import os
import shutil

import yaml.parser

"""
1. Написать скрипт, создающий стартер (заготовку) для проекта.
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?
2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта.
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
ситуации, библиотеки использовать нельзя.
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
«руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку.
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
расположены в родительских папках (они играют роль пространств имён); предусмотреть
возможные исключительные ситуации; это реальная задача, которая решена, например, во
фреймворке django.
"""


def recursive_walk(data, path=''):
    if isinstance(data, list):
        for val in data:
            if isinstance(val, str) and not os.path.exists(os.path.join(path, val)):
                open(os.path.join(path, val), 'w').close()
            else:
                recursive_walk(val, path)
    elif isinstance(data, dict):
        for key, val in data.items():
            if not os.path.exists(os.path.join(path, key)):
                os.mkdir(os.path.join(path, key))
            recursive_walk(data[key], os.path.join(path, key))


def normalize_templates(path):
    template_path = os.path.join(path, 'templates')
    if not os.path.exists(template_path):
        os.mkdir(template_path)
    for root, dirs, files in os.walk(path):
        if os.path.split(root)[-1] == 'templates':
            for folder in os.scandir(root):
                if not os.path.exists(os.path.join(template_path, folder.name)):
                    shutil.move(os.path.join(root, folder.name), template_path)
                    os.rmdir(root)


try:
    with open('config.yaml', encoding='utf-8') as yaml_config:
        project = yaml.safe_load(yaml_config)
    recursive_walk(project)
    normalize_templates(next(iter(project)))
    with open('config.json', encoding='utf-8') as json_config:
        project = json.load(json_config)
    recursive_walk(project)
    normalize_templates(next(iter(project)))
except FileNotFoundError:
    print('file does not exist')
except json.decoder.JSONDecodeError:
    print('json format error')
except yaml.parser.ParserError:
    print('yaml format error')
