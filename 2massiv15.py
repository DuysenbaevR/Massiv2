#26) Даны две квадратных таблицы чисел.
# Требуется построить третью, каждый элемент которой равен сумме элементов, стоящих на том же месте
#в 1-й и 2-й таблицах.
import random

a = []
n = int(input('Massiv olshemin kirtin: '))
for i in range(n):
    b = []
    for i2 in range(n):
        b.append(random.randrange(10))
    a.append(b)
c = []
for k in range(n):
    d = []
    for k2 in range(n):
        d.append(random.randrange(10))
    c.append(d)
e = []
for j in range(n):
    o = []
    for l in range(n):
        o.append(a[j][l] + c[j][l])
    e.append(o)
for q in a:
    print(*q)
print("/*/*/*/*//*/*/*/*/*/*/*/*/*/*/")
for p in c:
    print(*p)
print("/*/*/*/*//*/*/*/*/*/*/*/*/*/*/")
for ___ in e:
    print(*___)