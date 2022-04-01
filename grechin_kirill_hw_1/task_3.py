# 3.Склонение слова

# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

for index in range(1, 101):
    if 5 <= index <= 20:
        print(f'{index} процентов')
    elif index % 10 == 1:
        print(f'{index} процент')
    elif 2 <= index % 10 <= 4:
        print(f'{index} процента')
    else:
        print(f'{index} процентов')