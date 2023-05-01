minimum_investment = int(input('Введите минимальную инвестицию: '))
mike_invests = int(input('Сколько может инвестировать Майк: '))
ivan_invests = int(input('Сколько может инвестировать Иван: '))

if mike_invests >= minimum_investment and ivan_invests >= minimum_investment:
    print(2)
elif mike_invests >= minimum_investment >= ivan_invests:
    print('Mike')
elif mike_invests <= minimum_investment <= ivan_invests:
    print('Ivan')
elif (mike_invests + ivan_invests) >= minimum_investment:
    print(1)
else:
    print(0)
