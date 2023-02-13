# 1) Дан массив ['a', 'b', 'c']. Добавьте ему в конец элементы 1, 2, 3.

a = ['a', 'b', 'c']
k = 1
for i in range(3):
    a.append(str(k))
    k += 1
print(a)