# 2. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал
# каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два
# раза больше журавликов, чем Петя и Сережа вместе?

s_bird = int(input("Enter the number of cranes: "))

if not s_bird % 2:
    print(f"Petya made {int(s_bird * 1 / 6)}, Katya made {int(s_bird * 4 / 6)}, Serega made {int(s_bird * 1 / 6)}")
else:
    print("Digit the number of cranes must be even")
