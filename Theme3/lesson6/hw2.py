import collections


def get_suffix(age):
    age_title = None

    if age % 10 == 0 or age % 10 > 4 or 10 < age % 100 < 20:
        age_title = 'лет'
    elif age % 10 == 1:
        age_title = 'год'
    elif 1 < age % 10 < 5:
        age_title = 'года'
    else:
        print('Неверный возраст')
        get_suffix(age)

    return age_title


def get_last_key():
    return collections.deque(pets, maxlen=1)[0]


def get_pet_key():
    key = int(input('Введите ID питомца: '))

    if key not in pets:
        print('Питомец не найден')
        return

    return key


def get_pet_name(key):
    return list(pets[key].keys())[0]


def pets_list():
    for key in pets.keys():
        if key:
            print(read(key))


def create():
    key = get_last_key() + 1

    name = input('Введите кличку питомца: ')
    pets[key] = dict()
    pets[key][name] = dict()

    pets[key][name]['Вид питомца'] = input('Вид питомца: ')
    pets[key][name]['Возраст питомца'] = int(input('Возраст питомца: '))
    pets[key][name]['Имя владельца'] = input('Имя владельца: ')

    print('Питомец успешно создан')


def read(key_pet=None):
    key = key_pet or get_pet_key()

    if not key:
        return

    pet_name = get_pet_name(key)
    pet = pets[key][pet_name]

    print(f'Это {pet["Вид питомца"]} по кличке {pet_name}. '
          f'Возраст питомца: {pet["Возраст питомца"]} {get_suffix(pet["Возраст питомца"])}. '
          f'Имя владельца: {pet["Имя владельца"]}')


def update():
    key = get_pet_key()

    if not key:
        return

    pet_name = get_pet_name(key)
    pet = pets[key][pet_name]

    name = input(f'Введите кличку питомца ({pet_name}): ')
    updated_pet = dict()

    pet['Вид питомца'] = input(f'Вид питомца ({pet["Вид питомца"]}): ')
    pet['Возраст питомца'] = int(input(f'Возраст питомца ({pet["Возраст питомца"]}): '))
    pet['Имя владельца'] = input(f'Имя владельца ({pet["Имя владельца"]}): ')

    updated_pet[name] = pet
    pets[key] = updated_pet

    print('Питомец успешно обновлён')


def delete():
    key = get_pet_key()

    if not key:
        return

    pets.pop(key)
    print('Питомец успешно удалён')


pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            }
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            }
        }
}
command = None

while command != 'stop':
    command = input('Введите команду: ')

    match command:
        case 'create':
            create()
        case 'read':
            read()
        case 'update':
            update()
        case 'delete':
            delete()
        case 'stop':
            print('Программа завершена')
        case _:
            print('Неизвестная команда')

print(pets_list())
