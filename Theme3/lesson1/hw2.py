import math

num = int(input('Введите натуральное число: '))
count_divided = 0

if num >= 2e9:
    print('Максимальное число не может превышать 2.000.000.000')
    exit()

for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
        count_divided += 1

        if i != math.sqrt(num):
            count_divided += 1

print(f'Количество натуральных делителей - {count_divided}')