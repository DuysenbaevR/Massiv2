#13) Определите в массиве A номер первого элемента, равного X.
#Определите номер первого элемента, равного X, в первой половине массива A (массив имеет чётное число элементов).
#Определите номер первого элемента, равного X, во второй половине массива A (массив имеет чётное число элементов).

import random

a = []
n = int(input('Massiv olshemin kiritin: '))
first = 0
second = 0
for i in range(n):
    a.append(random.randrange(10, 50))
print(a)
x = int(input('X ti kiritin: '))
first = a.index(x)
second = a.index(x, int(n/2), int(n))
print(f"Birinshi yarimdagi X tin nomeri: {first + 1}")
print(f"Ekinshi yarimdagi X tin nomeri: {second + 1}")