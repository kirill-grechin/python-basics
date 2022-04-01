# 5. Создать вручную список, содержащий цены на товары (10-20 товаров):

price_list = [57.8, 46.51, 97, 102.67, 23.65, 67, 78.25, 75.31, 11.11, 71]

# A. Вывести на экран эти цены через запятую в одну строку.
# Цена должна отображаться в виде <r> руб <kk> коп (например "5 руб 04 коп").
# Подумать, как из цены получить рубли и копейки.
# Как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 08 коп или 00 коп).

for price in price_list:
    split_price = f'{price:.02f}'.split('.')
    print(f'{split_price[0]} руб {split_price[1]} коп', end=', ')

# B. Вывести цены, отсортированные по возрастанию, новый список не создавать.
# Доказать, что объект списка после сортировки остался тот же.

print(f'\n{id(price_list)}')

for price in sorted(price_list):
    print(price, end=' ')

print(f'\n{id(price_list)}')

# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.

new_price_list = sorted(price_list)[::-1]

print(new_price_list)

# D. Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

# В отсортированном по убыванию списке:

for price in new_price_list[0:5]:
    print(price, end=' ')

# В неотсортированном списке:

for price in sorted(price_list)[:-6:-1]:
    print(price, end=' ')
