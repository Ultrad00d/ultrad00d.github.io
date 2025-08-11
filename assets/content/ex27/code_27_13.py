from math import dist

# Альтернативный варинат генерации переменной для кластеров
clustersA = [[], []] # <-- в условии сказано, что в файле A 2 кластера 
clustersB = [[], [], []] # <-- в условии сказано, что в файле B 3 кластера

for line in open('uncompressed/assets/content/ex27/27_A.txt'):
    x, y = map(float, line.replace(',', '.').split())
    if y < 15:                      # <-- отбираем кластеры файла A
        clustersA[0].append([x, y]) #     уравнением через Excel
    else:                           #     (см. выше)
        clustersA[1].append([x, y])

for line in open('uncompressed/assets/content/ex27/27_B.txt'):
    x, y = map(float, line.replace(',', '.').split())
    if 5 < x < 10:                  # <-- отбираем кластеры файла B
        clustersB[0].append([x, y]) #     уравнением через Excel 
    elif 15 < x < 19:               # <-- (см. выше)
        clustersB[1].append([x, y])
    elif 20 < x < 24:
        clustersB[2].append([x, y])

# функция по нахождению центра кластера
def center(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA] # все центры кластеров файла A
centersB = [center(cl) for cl in clustersB] # все центры кластеров файла B
Px = abs(int(sum(x for x, y in centersA) * 10_000))
Py = abs(int(sum(y for x, y in centersA) * 10_000))
print(Px, Py)

Q1 = abs(int(min(dist(cl1, cl2) for cl1 in centersB for cl2 in centersB if cl1 != cl2) * 10_000))
Q2 = abs(int(max(dist(cl1, cl2) for cl1 in centersB for cl2 in centersB if cl1 != cl2) * 10_000))
print(Q1, Q2)