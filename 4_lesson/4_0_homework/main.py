# 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств
#
# Пример:
#
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
import random


def create_array(sz: int, st: int, lt: int):
    array = list()
    for _ in range(sz):
        array.append(random.randint(st, lt))
    return array


if __name__ == "__main__":
    size1, size2 = input("Please, enter size 1 and 2 array: ").split()
    start1, start2 = input("Please, enter start digit in 1 array and 2 array for random generator: ").split()
    last1, last2 = input("Please, enter last digit in 1 array and 2 array for random generator: ").split()
    list_arr1 = create_array(int(size1), int(start1), int(last1))
    list_arr2 = create_array(int(size2), int(start2), int(last2))
    print(*list_arr1)
    print(*list_arr2)
    print(*sorted(set(list_arr1).intersection(set(list_arr2))))
