#14) Заполнить массив из 10 элементов случайными числами в интервале [-10..10]
# и сделать реверс отдельно для 1-ой и 2-ой половин массива.

import random
n = int(input('Massiv olshemin kiritin: '))
a = []
for i in range(n):
    a.append(random.randrange(-10, 10))
print(a)
print("/*/**/*/*/*/*/*/*/*/*/*/")
b = []
for j in range(n):
    if j <= n/2:
        b.append(a[int(n/2) - 1 - j])
    else:
        b.append(a[int(n + n/2) - 1 - j])
print(b)