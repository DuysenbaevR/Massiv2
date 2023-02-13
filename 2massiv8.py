#12) Заполнить массив из 10 элементов случайными числами в интервале [0..4] и определить,
# есть ли в нем одинаковые соседние элементы.

import random

a = []
for i in range(10):
    a.append(random.randrange(0, 4))
print(a)
for i in range(9):
    if a[i] == a[i + 1]:
        print(a[i])