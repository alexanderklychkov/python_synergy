pets = dict()
name = input('Введите кличку питомца: ')
pets[name] = dict()

pets[name]['Вид питомца'] = input('Вид питомца: ')
pets[name]['Возраст питомца'] = int(input('Возраст питомца: '))
pets[name]['Имя владельца'] = input('Имя владельца: ')

list_pet = list(pets[name].items())
age = pets[name]['Возраст питомца']
age_title = None

if age % 10 == 0 or age % 10 > 4 or 10 < age % 100 < 20:
    age_title = 'лет'
elif age % 10 == 1:
    age_title = 'год'
elif 1 < age % 10 < 5:
    age_title = 'года'
else:
    print('Неверный возраст')
    exit()

print(f'Это {list_pet[0][1]} по кличке {name}. '
      f'{list_pet[1][0]}: {list_pet[1][1]} {age_title}. '
      f'{list_pet[2][0]}: {list_pet[2][1]}')
