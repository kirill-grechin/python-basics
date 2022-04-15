from functools import wraps


# Написать декоратор для логирования типов позиционных аргументов функции
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
# ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
# аргументов? Сможете ли вы замаскировать работу декоратора?

def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            print(f'{func.__name__}({arg}: {type(arg)})', end=',')
        return func(*args, **kwargs)

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    return tuple(map(lambda x: x ** 3, list(args) + list(kwargs.values())))


print(calc_cube(1, 5, 6, 7, i=10, j=15))
print(calc_cube(12, 16, 19, 20, 1, 15, 15))
