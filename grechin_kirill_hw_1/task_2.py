# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

nums_list = []

for number in range(1, 1000, 2):
    nums_list.append(number ** 3)

print(nums_list)


# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!

def calculate_sum(my_list):
    total_sum = 0

    for num in my_list:
        num_sum = 0
        num_copy = num

        while num_copy > 0:
            digit = num_copy % 10
            num_sum += digit
            num_copy //= 10

        if num_sum % 7 == 0:
            total_sum += num

    return total_sum


print(f'Сумма чисел: {calculate_sum(nums_list)}')

# b. К каждому элементу списка добавить 17.

new_nums_list = []

for number in nums_list:
    new_nums_list.append(number + 17)

print(new_nums_list)

# c. * Решить задачу под пунктом b, не создавая новый список.

for index, number in enumerate(nums_list):
    nums_list[index] = number + 17

print(nums_list)

# Заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

print(f'Сумма чисел: {calculate_sum(nums_list)}')
