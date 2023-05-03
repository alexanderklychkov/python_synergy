text = input('Введите строку без пробелов: ')
text_revert = text[len(text) - 1::-1]

if text == text_revert:
    print('yes')
else:
    print('no')
