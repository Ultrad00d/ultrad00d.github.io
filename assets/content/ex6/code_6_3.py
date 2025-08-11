from turtle import *

screensize(3000, 3000)
tracer(0)
m = 40
left(90)

for _ in range(5):
    circle(5 * m, 180)
    rt(90)
    circle(5 * m, 180)
    rt(90)
    circle(5 * m, 180)
    rt(90)
    circle(5 * m, 180)
    rt(90)

pu()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(x * m, y * m)
        dot(5)
done()