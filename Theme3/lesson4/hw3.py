mass = list(map(int, input(f'Введите числа через пробел: ').split()))
mass_set = set()

for el in mass:
    if el in mass_set:
        print('YES')
    else:
        print('NO')

    mass_set.add(el)
