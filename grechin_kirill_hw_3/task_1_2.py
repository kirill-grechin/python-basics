translator = {
    'one': 'один', 'two': 'два',
    'three': 'три', 'four': 'четыре',
    'five': 'пять', 'six': 'шесть',
    'seven': 'семь', 'eight': 'восемь',
    'nine': 'девять', 'ten': 'десять'
}


# 1. Написать функцию num_translate().
# Функция переводит числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть None.


def num_translate(key):
    return translator.get(key)


print(num_translate('one'), num_translate('five'), num_translate('key'))


# 2. *Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
# должен быть с заглавной.


def num_translate_adv(key):
    value = translator.get(key.lower())
    return value.capitalize() if key.istitle() and value else value


print(num_translate_adv('two'), num_translate_adv('key'), num_translate_adv('Three'), num_translate_adv('Key'))
