from turtle import *

screensize(3000, 3000)
tracer(0)
m = 40
left(90)

for _ in range(7):
    fd(10 * m)
    rt(120)

pu()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(x * m, y * m)
        dot(5)
done()