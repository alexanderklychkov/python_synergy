word = input('Введите слово из маленьких латинских букв: ')
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
vowels_count = 0
consonants_dict = {}
consonants_count = 0
has_all_letters = True

for symbol in word:
    if symbol in vowels:
        vowels_dict[symbol] += 1
    elif symbol in consonants_dict:
        consonants_dict[symbol] += 1
    else:
        consonants_dict[symbol] = 1

for vowel in vowels_dict:
    if vowels_dict[vowel] == 0:
        has_all_letters = False

for vowel in vowels_dict:
    vowels_count += vowels_dict[vowel]
    print(f'Количество гласной {vowel}: {vowels_dict[vowel]}')

for consonant in consonants_dict:
    consonants_count += consonants_dict[consonant]
    print(f'Количество согласной {consonant}: {consonants_dict[consonant]}')


print(f'\nОбщее количество гласных - {vowels_count}')
print(f'Общее количество согласных - {consonants_count}')

if not has_all_letters:
    print(False)
