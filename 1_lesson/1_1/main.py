# 2. В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся
# в каждом из трех классов. Выведите наименьшее число
# парт, которое нужно приобрести для них.

klass1_parts = int(input("Сколько учеников в первом классе:"))
klass2_parts = int(input("Сколько учеников во втором классе:"))
klass3_parts = int(input("Сколько учеников во втором классе:"))
parts = -(-klass1_parts // 2) + -(-klass2_parts // 2) + -(-klass3_parts // 2)
print(f"Необходимо {parts} парт(ы)")
