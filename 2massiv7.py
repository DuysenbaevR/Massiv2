 #11) Дан массив из N элементов в диапазоне [100;300].
# Сжать массив, оставив в нем только те элементы, сумма цифр которых четная.
import random

a = []
count = 0
n = int(input('Massv olshemin kiritin: '))
for i in range(n):
    a.append(random.randrange(100, 300))
print(a)
print("/*/*/*/*/*/*/*/*/*/*/*/")
for j in range(n - count):
    sum = int(a[j]/100) + int(int(a[j]/10) % 10) + int(a[j] % 10)
    if sum % 2 == 1:
        del a[j]
        count += 1
    sum = 0
print(a)