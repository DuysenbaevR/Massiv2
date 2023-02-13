#15) Заполнить массив из 12 элементов случайными числами в интервале [-12..12]
# и выполнить циклический сдвиг ВПРАВО на 4 элемента.
import random

a = []
for i in range(12):
  a.append(random.randrange(-12, 12))
print(a)
b = []
for i in range(8, 12):
  b.append(a[i])
for i in range(0, 8):
  b.append(a[i])
print(b)