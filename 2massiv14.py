#25) Получить среднее арифметическое всех чётных элементов массива, стоящих на нечётных местах.

import random

a = []
n = int(input('Massiv olshemin kiritin: '))
sum = 0

for i in range(n):
    a.append(random.randrange(10))
print(a)
k = 1
count = 0
while k < n:
    if a[k] % 2 == 0:
        sum += a[k]
        count += 1
    k += 2
print(f"Taq orindagi jup elementler orta arifmetigi: {sum / count}")