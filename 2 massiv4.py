#7) Найти максимальный элемент массива и его индекс (max_num   и   max_index).
import random
n = int(input('Massiv olshemin kiritin: '))
a = []
for i in range(n):
    a.append(random.randrange(10, 25))
print(f"{a}")
print(f"Maksimal element: {max(a)}")
print(f"Maksimal element indexi: {a.index(max(a))}")