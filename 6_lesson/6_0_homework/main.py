# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Please, enter first digit: "))
dificult = int(input("Please, enter dificult digit: "))
n = int(input("Please, enter amount of digit: "))

for i in range(n):
    print(a1 + i * dificult, end=" ")
