list_one = int(input('Введите кол-во чисел для 1 списка: '))

if list_one > 100000:
    print('Превышено максимальное значение')
    exit()

list_one_set = set()

for i in range(list_one):
    list_one_set.add(int(input('Введите число: ')))

list_two = int(input('Введите кол-во чисел для 2 списка: '))
list_two_set = set()

for i in range(list_two):
    list_two_set.add(int(input('Введите число: ')))

print(f'Кол-во одинаковых чисел в 1 и 2 списке - {len(list_one_set.intersection(list_two_set))}')
