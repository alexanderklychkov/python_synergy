def printer(arr, idx=0):
    if idx > len(arr) - 1:
        print('Конец списка')
        return

    print(arr[idx])
    printer(arr, idx + 1)


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
printer(my_list)
