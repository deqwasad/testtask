from random import randint
n = int(input())
a = []
c = []
k = 0
for i in range(n):
    m = randint(1, n)
    while k < len(c):
        if m == c[k]:
            k = 0
            m = randint(1, n)
        else:
            k += 1
    c.append(m)
    k = 0
    b = []
    for j in range(m):
        x = randint(1, n)
        b.append(x)
    z = i % 2
    if z == 1:
        b = sorted(b)
    else:
        b = sorted(b, reverse=True)
    a.append(b)
print(c) # размеры полученных массивов
print(a) # ответ
