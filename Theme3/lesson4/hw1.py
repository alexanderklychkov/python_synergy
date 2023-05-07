n = int(input('Введите кол-во чисел: '))

if not 1 <= n <= 100000:
    print('Число должно быть в диапазоне от 1 до 100000')
    exit()

arr = set()

for i in range(n):
    num = int(input(f'Введите число для {i} индекса: '))

    if num > 2 * 10e9:
        print('Превышено максимальное значение')
        exit()

    arr.add(num)

print(f'Кол-во различных чисел - {len(arr)}')
