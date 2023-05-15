def get_factorial(num):
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    return factorial


def get_factorial_list(num):
    arr = []

    for i in range(num, 0, -1):
        arr.append(i)

    return arr


user_num = int(input('Введите натуральное целое число: '))
factorial_list = []

for el in get_factorial_list(get_factorial(user_num)):
    factorial_list.append(get_factorial(el))

print(factorial_list)
