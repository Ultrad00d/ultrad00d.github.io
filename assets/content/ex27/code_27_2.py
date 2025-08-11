# Обычная функция по поиску расстояния
def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# или просто 
from math import dist

# Пример нестандартной функции по поиску расстояния
def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return max(abs(x2 - x1), abs(y2 - y1))