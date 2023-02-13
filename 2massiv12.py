#16) Вывести элементы числового массива, которые больше, чем элементы, стоящие перед ними.
#Например, дан массив [3, 9, 8, 4, 5, 1].
# Следует вывести числа 9 и 5, так как перед ними стоят соответственно числа 3 и 4, которые меньше их.

import random

a = []
n = int(input('Massiv olshemin kiritin: '))
for i in range(n):
    a.append(random.randrange(20))
print(a)
for k in range(n - 1):
    if a[k] < a[k + 1]:
        print(a[k + 1])