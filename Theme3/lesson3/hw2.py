n = int(input('Введите кол-во чисел: '))

if not 1 <= n <= 100000:
    print('Значение должно быть в диапазоне от 1 до 100000')
    exit()

mass = list(map(int, input(f'Введите {n} чисел через пробел: ').split()))

if len(mass) > n:
    print(f'Кол-во чисел не может быть больше {n}')
    exit()

new_mass = []

for i in range(-1, len(mass) - 1):
    new_mass.append(mass[i])


print(mass)
print(new_mass)
