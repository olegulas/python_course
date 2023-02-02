# Найдите сумму цифр трехзначного числа.
# in
# 123
# out
# 6
# про while в условии темы ничего несказано,
# значит использовать нельзя, и конструкция отмечена только в теме семинара № 2

n_threedigit = int(input("Enter three-digit number: "))
s_3digit = 0

s_3digit += n_threedigit % 10
n_threedigit //= 10
s_3digit += n_threedigit % 10
n_threedigit //= 10
s_3digit += n_threedigit

print(s_3digit)