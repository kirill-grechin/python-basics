def print_dictionary(dictionary):
    [print(key, ':', val) for key, val in dictionary.items()]


# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.
# Как поступить, если потребуется сортировка по ключам?


def thesaurus(*args):
    dictionary = {}
    for item in sorted(set(args)):  # set: без повторений, sorted: ключ, значение добавляются в алфавитном порядке
        dictionary.setdefault(item[0], []).append(item)
    return dictionary  # отсортированный словарь по ключам и значениям


print_dictionary(thesaurus('Иван', 'Владимир', 'Олег', 'Николай', 'Марина', 'Юлия', 'Евгения',
                           'Ирина', 'Василий', 'Кирилл', 'Егор', 'Наталья', 'Александр', 'Василий'))


# 4. *Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
# фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы.
# Как поступить, если потребуется сортировка по ключам?


def thesaurus_adv(*args):
    dictionary = {}
    for item in sorted(set(args)):  # внутренние словари будут отсортированы по алфавиту (ключи и значения)
        dictionary.setdefault(item.split()[1][0], {}).setdefault(item.split()[0][0], []).append(item)
    return dict(sorted(dictionary.items()))  # сортировка ключей общего словаря


print_dictionary(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов',
                               'Анна Савельева', 'Владимир Быстров', 'Иван Сидоров', 'Сергей Орлов',
                               'Илья Иванов', 'Евгения Алексеева', 'Кирилл Бобров'))