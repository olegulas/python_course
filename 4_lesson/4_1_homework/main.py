# 2. В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
#
# Пример:
#
# 4 -> 1 2 3 4
# 9
import random


def create_array(sz: int, st: int, lt: int):
    array = list()
    for _ in range(sz):
        array.append(random.randint(st, lt))
    return array


def max_buches(arr):
    max_bushes = 0
    for item in range(n):
        sum_buches = arr[item - 1] + arr[item] + arr[item + 1 if item < n - 1 else 0]
        if max_bushes < sum_buches:
            max_bushes = sum_buches
    return max_bushes


if __name__ == "__main__":
    n = int(input("please enter the number of bushes: "))
    start = int(input("Please, enter start digit in array bushes for random generator: "))
    last = int(input("Please, enter last digit in array bushes for random generator: "))
    list_arr = create_array(n, start, last)
    print(*list_arr)
    print(max_buches(list_arr))
