import math

m = int(input('Введите какой максимальный вес в кг может выдержать лодка: '))

if not 1 <= m <= 10e6:
    print('Превышен максимальный вес')
    exit()

b = int(input('Введите кол-во рыбаков: '))

if not 1 <= b <= 100:
    print('Превышено максимальное кол-во рыбаков')
    exit()

weight_mass = []
common_weight = 0

for i in range(b):
    weight = int(input(f'Вес {i + 1} рыбака: '))

    if not 1 <= weight <= m:
        print('Превышен максимальный вес рыбака')
        exit()

    weight_mass.append(weight)
    common_weight += weight

print(f'Минимальное кол-во лодок для перевозки - {math.ceil(common_weight / m)}')
