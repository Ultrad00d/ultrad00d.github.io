def convert(n):
    n3 = ''
    while n > 0:
        n, rem = divmod(n, 3)
        n3 = str(rem) + n3
    return n3