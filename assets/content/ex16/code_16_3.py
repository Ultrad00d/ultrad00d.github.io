def f(n):
    if n >= 100: return 100
    return f(n + 1) - 1

print(f(10))
# f(10) = f(11) - 1 = (f(12) - 1) - 1 = ...
# 10