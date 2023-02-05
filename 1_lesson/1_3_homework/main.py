# 4. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один
# разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Enter n amount slice chocolade: "))
m = int(input("Enter n amount slice chocolade: "))
k = int(input("Enter k amount slice which you can eat: "))

if (k % n == 0 or k % m == 0) and (k < n * m):
    print("Yes, you can")
else:
    print("No, you can't do it")
