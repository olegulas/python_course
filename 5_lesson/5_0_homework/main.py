# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью
# рекурсии.
def pow_ab(val1, val2):
    if val2 == 0:
        return 1
    if val2 < 0:
        return pow_ab(val1, val2 + 1) * 1 / val1
    return pow_ab(val1, val2 - 1) * val1


if __name__ == "__main__":
    a = int(input("Please, enter digit: "))
    a_pow = int(input("Please enter the degree of the number: "))
    print(f"{a}**{a_pow} = {pow_ab(a, a_pow)}")
