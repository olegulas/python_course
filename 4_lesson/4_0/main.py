# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

enter_str = input("Please, enter string symbols = ").split()
dict_str = {}.fromkeys(enter_str, 0)

for item in enter_str:
    print(f"{item}_{dict_str[item]}" if dict_str[item] else item, end=" ")
    dict_str[item] += 1
