# 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних
# трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.

n_ticket = input("Enter the number of ticket: ")
sum_num1 = sum_num2 = 0

if 1 < len(n_ticket) < 7:
    num2 = n_ticket % 1000
    num1 = n_ticket // 1000

    sum_num1 += num1 % 10
    num1 //= 10
    sum_num1 += num1 % 10
    num1 //= 10
    sum_num1 += num1 % 10

    sum_num2 += num2 % 10
    num2 //= 10
    sum_num2 += num2 % 10
    num2 //= 10
    sum_num2 += num2 % 10

    if sum_num1 == sum_num2:
        print("You are lucky man!")
    else:
        print("Sorry, buy a new ticket, this unlucky!")
else:
    print("Please, enter the correct number - 6 digit")
