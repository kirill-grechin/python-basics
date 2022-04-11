from functools import wraps


# Написать декоратор для логирования типов позиционных аргументов функции
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
# ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
# аргументов? Сможете ли вы замаскировать работу декоратора?

def type_logger_cacher(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        cache.update({arg: type(arg) for arg in set(args) if arg not in cache})
        cache.update({arg: type(arg) for arg in set(kwargs.values()) if arg not in cache})
        return ', '.join(f'{func.__name__}({arg}: {cache[arg]})' for arg in list(args) + list(kwargs.values()))

    return wrapper


@type_logger_cacher
def calc_cube(*args, **kwargs):
    return tuple([arg ** 3 for arg in args] + [(arg1, arg2 ** 3) for arg1, arg2 in kwargs.items()])


print(calc_cube(1, 5, 6, 7, i=10, j=15))
print(calc_cube(12, 16, 19, 20, 1, 15, 15))
