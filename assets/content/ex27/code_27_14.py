data = []

# Заменим на '27_B.txt' после файла A
for line in open('27_A.txt'):
    x, y = map(float, line.split())
    data.append([x, y])

from math import dist
clusters = []

while data:
    cl = [data.pop()]
    for p in cl:
        n = [p1 for p1 in data if dist(p, p1) < 2]
        cl += n
        for p1 in n: data.remove(p1)
    clusters.append(cl)

print([len(cl) for cl in clusters])

def center(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]

centers = [center(cl) for cl in clusters]
# Добавить комментарий для файла A
Px = abs(int(sum(x for x, y in centers) * 10_000))
Py = abs(int(sum(y for x, y in centers) * 10_000))
print(Px, Py)

# Убрать комментарий для файла B
# Q1 = abs(int(min(dist(cl1, cl2) for cl1 in centers for cl2 in centers if cl1 != cl2) * 10_000))
# Q2 = abs(int(max(dist(cl1, cl2) for cl1 in centers for cl2 in centers if cl1 != cl2) * 10_000))
# print(Q1, Q2)

# Проверка черепашкой
from turtle import *
pu()
m = 30
tracer(0)
screensize(3000, 3000)
colors = ['pink', 'blue', 'lime']
for i in range(3):
    for x, y in clusters[i]:
        color(colors[i])
        goto(x * m, y * m)
        dot(2)
done()