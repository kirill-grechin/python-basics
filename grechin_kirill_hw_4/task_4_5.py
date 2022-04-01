import utils
import sys

if len(sys.argv) != 2:
    # 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
    # Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
    # Убедиться, что ничего лишнего не происходит.

    print(utils.currency_rates_adv('USD'), utils.currency_rates_adv('eur'), utils.currency_rates_adv('cnf'))
else:
    # 5. *Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.

    val_conv = utils.currency_rates_adv(sys.argv[1])
    print(f'date: {val_conv.get("date")} value: {val_conv.get("value")}') if val_conv else print(val_conv)
