print('Набор чисел для 1 списка')
list_one = set()

for i in range(5):
    list_one.add(int(input('Введите число: ')))

print('Набор чисел для 2 списка')
list_two = set()

for i in range(5):
    list_two.add(int(input('Введите число: ')))

print(f'Кол-во одинаковых чисел в 1 и 2 списке - {len(list_one.intersection(list_two))}')
