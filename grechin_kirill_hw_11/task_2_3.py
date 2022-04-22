class MyZeroDivisionError(Exception):
    def __init__(self, message):
        self.message = message


num_1, num_2 = int(input('Введите левый операнд: ')), int(input('Введите правый операнд: '))

try:
    if num_2 == 0:
        raise MyZeroDivisionError('Ошибка: правый операнд равен 0')
except MyZeroDivisionError as ex:
    print(ex)


class MyIntegerOnlyListError(Exception):
    def __init__(self, message):
        self.message = message


nums = []
while True:
    data = input('Введите значение для добавления в список: ')
    try:
        if data == 'stop':
            break
        if not data.isdigit():
            raise MyZeroDivisionError('Ошибка: лист может содержать только числа')
        else:
            nums.append(int(data))
    except MyZeroDivisionError as ex:
        print(ex)
print(nums)
