a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
str_numbers = ''

if not a <= b:
    print('B должно быть больше, чем А')
    exit()

for i in range(a, b + 1):
    if i % 2 == 0:
        str_numbers += f' {i}'

print(f'Четные числа на заданном отрезке:{str_numbers}')
