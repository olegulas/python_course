# 2. Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
#
# Пример:
#
# 4 4 -> 2 2
# 5 6 -> 2 3

sum_x1x2 = int(input("Enter sum x1 + x2: "))
p_x1x2 = int(input("Enter composition x1 * x2: "))
# formula x2**2 - sum_x1x2 * x2 + p_x1x2 = 0
discriminant = sum_x1x2 ** 2 - 4 * p_x1x2
if discriminant > 0:
    x1 = (sum_x1x2 + discriminant ** (1 / 2)) / 2
    x2 = (sum_x1x2 - discriminant ** (1 / 2)) / 2
elif discriminant == 0:
    x1 = x2 = sum_x1x2 / 2
else:
    print("task not have result, because is wrong condition!")
    exit()
print(f"{x1:.0f} {x2:.0f}")
