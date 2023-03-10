# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе
# несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

vowels = "АЕЁИОУЫЭЮЯ"

vinni_poem = input("Please, enter a poem of Vini-puh: ").split()

poem_let = [word.count(char) for word in vinni_poem for char in word if char.upper() in vowels]

if len(set(poem_let)) == 1:
    print("Парам пам-пам, - your rhythm is good")
else:
    print("Пам парам, - your rhythm is bad")