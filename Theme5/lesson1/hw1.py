import math


class CashRegister(object):
    __count = 0

    def top_up(self, x):
        self.__count += x

    def count_1000(self):
        return math.floor(self.__count / 1000)

    def take_away(self, x):
        if x > self.__count:
            print('Недостаточно денег')
            return

        self.__count -= x


cash_register = CashRegister()
cash_register.top_up(3500)
cash_register.take_away(300)
print(cash_register.count_1000())