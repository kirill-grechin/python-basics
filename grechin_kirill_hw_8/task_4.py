from functools import wraps


# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
# значения функции и выбрасывать исключение ValueError, если что-то не так.

def val_checker(check):
    def _val_checker(func):
        @wraps(func)
        def wrapper(number):
            if not check(number):
                raise ValueError(f'Wrong val: {number}')
            return func(number)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    print(calc_cube(5))
    print(calc_cube(-1))
except ValueError as ve:
    print(ve)
