num = int(input())
parity_num_str = None
integer_num_str = None

if num % 2 == 0:
    parity_num_str = 'четное'
else:
    parity_num_str = 'нечетное'

if num < 0:
    integer_num_str = 'отрицательное'
elif num > 0:
    integer_num_str = 'положительное'
else:
    integer_num_str = 'нулевое'
    parity_num_str = ''

print(f'{integer_num_str} {parity_num_str} число')