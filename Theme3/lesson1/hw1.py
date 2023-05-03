num = int(input('Введите число символов: '))
count_zero = 0

for i in range(num):
    n = int(input(f'Введите число для {i} элемента: '))

    if n == 0:
        count_zero += 1

print(f'Количество нулей - {count_zero}')
