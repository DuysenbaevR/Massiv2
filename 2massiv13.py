#22) В массиве найти минимальное значение среди элементов с нечетными индексами.

import random
a = []
n = int(input('Massiv olshemin kiritin: '))
for i in range(n):
    a.append(random.randrange(10))
print(a)
k = 1
min = a[1]
while k < n:
    if a[k] < min:
        min = a[k]
    k += 2
print(f"Taq indeksli Minimum element: {min}")