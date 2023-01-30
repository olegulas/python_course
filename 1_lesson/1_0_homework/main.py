# Найдите сумму цифр трехзначного числа.
# in
# 123
# out
# 6

n_threedigit = int(input("Enter three-digit number: "))
s_3digit = 0

s_3digit += n_threedigit % 10
n_threedigit //= 10
s_3digit += n_threedigit % 10
n_threedigit //= 10
s_3digit += n_threedigit

print(s_3digit)
