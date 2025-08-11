def f(n):
    if n <= 0: return 0
    return f(n - 1) + 1

print(f(10))
# f(10) = f(9) + 1 = (f(8) + 1) + 1 = ...
# 10