# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических
# операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum_new(num1, num2):
    if num1 == 0:
        return num2
    return sum_new(num1 - 1, num2 + 1)


if __name__ == "__main__":
    a = int(input("Please, enter digit A: "))
    b = int(input("Please, enter digit B: "))
    print(f"{a} + {b} = {sum_new(a, b)}")
