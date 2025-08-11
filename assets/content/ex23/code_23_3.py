def f(x, end):
    if x > end: return 0
    if x == end: return 1
    if x == 56: return 0
    return f(x + 3, end) + f(x + 7, end) + f(x * 3, end)

# аналогично задаче выше, тк нужно прохождение через число,
# то мы считаем кол-во траекторий до него
print(f(12, 40) * f(40, 72) * f(72, 89))