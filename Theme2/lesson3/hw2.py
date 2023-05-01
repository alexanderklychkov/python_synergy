word = input('Введите слово из маленьких латинских букв: ')
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
has_all_letters = True

for symbol in word:
    if symbol in vowels:
        vowels_dict[symbol] += 1

for vowel in vowels_dict:
    if vowels_dict[vowel] == 0:
        has_all_letters = False

if has_all_letters:
    for vowel in vowels_dict:
        print(f'Количество {vowel}: {vowels_dict[vowel]}')
else:
    print(False)
