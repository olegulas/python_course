# 2 Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
#
# Пример:
#
# 5
# 1 2 3 4 5
# 6
# -> 5
import random


def create_array(sz: int, st: int, lt: int):
    array = list()
    for _ in range(sz):
        array.append(random.randint(st, lt))
    return array


def find_count_num_in_array(find: list, find_num):
    close_num = find[0]
    for i in find:
        if abs(find_num - i) < abs(find_num - close_num):
            close_num = i
    return close_num


if __name__ == "__main__":
    size = int(input("Please, enter size array: "))
    start = int(input("Please, enter start digit for random generator: "))
    last = int(input("Please, enter last digit for random generator: "))
    list_arr = create_array(size, start, last)
    print(list_arr)
    find_num_count = int(input("Please, digit X for for find in array: "))
    print(find_count_num_in_array(list_arr, find_num_count))
