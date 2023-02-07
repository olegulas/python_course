# 3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#
# Пример:
#
# 10 -> 1 2 4 8

n = int(input("Enter n = "))
res_2k = pow_2k = 0
while res_2k < n:
    res_2k = 2 ** pow_2k
    if res_2k > n:
        exit()
    print(res_2k, end=' ')
    pow_2k += 1
