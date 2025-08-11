def f(x, y, a):
    # переписываем функцию из условия
    return (x < a) and (y < 3 * a) or (2 * x + y > 128)

# перебираем ашки, иксы и игрики и проверяем,
# чтобы для них всех выполнялась функция:
for a in range(1, 200):
    if all(f(x, y, a) for x in range(1, 200) for y in range(1, 200)):
        print(a)
        break