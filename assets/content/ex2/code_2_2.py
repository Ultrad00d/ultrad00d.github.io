...
if all(f1(**dict(zip(p, line))) == line[-1] for line in t):
    if all(f2(**dict(zip(p, line))) == line[-1] for line in t):
        print(*p)