# прочитаем файл
for line in open('file_27.txt'):
    # получим из строки x, y
    x, y = map(float, line.replace(',', '.').split())
    
    # Дополнительные условия для координат, например:
    if x < 0 and -1 < y < 1:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])
