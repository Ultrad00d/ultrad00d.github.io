# создаем стандартную черепашку из номера 6
from turtle import *

pu()
m = 30
tracer(0)
screensize(3000, 3000)
# сколько кластеров, столько и цветов:
colors = ['pink', 'blue', 'lime']
# можно выбрать из:
#   "red", "green", "blue", "yellow", "cyan", "magenta",
#   "black", "white", "orange", "purple", "pink", "brown",
#   "gray", "lightgray", "darkgray", "gold", "silver",
 #  "lime", "maroon", "navy", "olive", "teal", "violet"

for i in range(штук_кластеров):
    for x, y in массив_с_кластерами[i]:
        color(colors[i])
        goto(x * m, y * m)
        dot(2)
done()