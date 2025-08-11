# в условии сказано, что в файле A 2 кластера 
clustersA = [[] for _ in range(2)]
# в условии сказано, что в файле B 3 кластера
clustersB = [[] for _ in range(3)]

# прочитаем файл A
for line in open('27_A.txt'):
    # получим из строки x, y
    x, y = map(float, line.replace(',', '.').split())
    # Теперь, разделим кластеры такими же выражениями, 
    # какие мы получили в Excel:
    if x < 0:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

# Аналогично для файла B
for line in open('27_B.txt'):
    x, y = map(float, line.replace(',', '.').split())
    if x < 0:
        clustersB[0].append([x, y])
    elif y > 4:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])