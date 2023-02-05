# 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
#
# Пример:
#
# 5 -> 1 0 1 1 0
# 2

n = int(input("Enter digit amount of coins: "))

side_0_coin = side_1_coin = 0
for _ in range(n):
    coin = int(input("Enter of coins: "))
    if coin == 0:
        side_0_coin += 1
    else:
        side_1_coin += 1
need_revert_0 = n - side_0_coin
need_revert_1 = n - side_1_coin
if need_revert_0 < need_revert_1:
    print(need_revert_0)
else:
    print(need_revert_1)
