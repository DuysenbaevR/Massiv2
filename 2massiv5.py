#9) Дан массив из 50 элементов и лежат в диапазоне от -50 до 49 включительно.
# Требуется из одного массива скопировать в другой массив значения в диапазоне от -5 до 5 включительно и подсчитать их количество.
import random

a = []
count = 0
copy = []
for i in range(50):
    a.append(random.randrange(-50, 49))
    if a[i] >= -5 and a[i] <= 5:
        copy.append(a[i])
        count += 1
print(a)
print(copy)
print(count)