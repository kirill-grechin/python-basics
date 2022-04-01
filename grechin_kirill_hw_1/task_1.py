# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:

# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# Подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности?

durs_count = int(input('Введите количество периодов: '))

for index in range(durs_count):
    duration = int(input(f'Введите {index + 1} период: '))

    days = duration // (3600 * 24)
    hours = (duration // 3600) % 24
    minutes = (duration // 60) % 60
    seconds = duration % 60

    date = [[days, 'дн'], [hours, 'час'], [minutes, 'мин'], [seconds, 'сек']]

    for unit, unit_name in date:
        if unit != 0:
            print(unit, unit_name, end=' ')
    print('\n')
