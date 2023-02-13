#10) В одномерном массиве (заполнение массива случайными числами от -50 до 49) найти сумму отрицательных элементов.
# Если эта сумма меньше -100, то необходимо прибавить к ней минимальный положительный элемент.

import random

a = []
copy = []
sum = 0
for i in range(50):
    a.append(random.randrange(-50, 49))
    if a[i] < 0:
        sum += a[i]
    else:
        copy.append(a[i])
print(a)
print(copy)
print(sum)
print(min(copy))
if sum < -100:
    print(sum + min(copy))