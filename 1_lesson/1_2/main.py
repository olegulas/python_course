# 3. Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон
# от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.

i = int(input("Введите в какой вагон зашел пассажир: "))
j = int(input("Введите в каком вагоне оказался пассажир: "))

if i == j:
    print(f"В поезде неизвестно количество  вагонов")
else:
    print(f"В поезде {i + j - 1} вагонов")