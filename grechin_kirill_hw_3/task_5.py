from random import sample, choices

# sample: генерирует k рандомных объектов из последовательности без повторов.
# choices: генерирует k рандомных объектов из последовательности с повторами.

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого).
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
# Документировать код функции.


def get_jokes(count=1, repeats=True):
    """
    Generate list of jokes for given count.

    :param count: count of jokes (default: 1)
    :param repeats: flag to repeat words from lists (default: True)
    :return list of string jokes or None (if repeats=False and count > len(nouns))
    """
    if repeats:
        zip_list = list(zip(choices(nouns, k=count), choices(adverbs, k=count), choices(adjectives, k=count)))
    else:
        if count > min(len(nouns), len(adverbs), len(adjectives)):
            return
        zip_list = list(zip(sample(nouns, k=count), sample(adverbs, k=count), sample(adjectives, k=count)))
    return [' '.join(x) for x in zip_list]


print(get_jokes(), get_jokes(10), get_jokes(5, repeats=False), sep='\n')
