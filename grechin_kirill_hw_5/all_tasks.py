from itertools import zip_longest
from random import randint


# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.

def odd_nums(limit):
    for num in range(1, limit + 1, 2):
        yield num


rng = randint(10, 100)
print(*(odd_nums(rng)))

# 2. Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

print(*(num for num in range(1, rng + 1, 2)))

# 3. Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, вывести последние кортежи в виде: (<tutor>, None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

zip_kit = zip_longest(tutors, klasses)
print(*zip_kit, *zip_kit)  # распечатает один раз

# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[index] for index in range(1, len(src)) if src[index] > src[index - 1]]
print(result)

# 5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [val for val in src if src.count(val) == 1]
print(result)
