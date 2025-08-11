def convert(n):
    n3 = ''
    while n > 0:
        n3 = str(n % 3) + n3
        n //= 3
    return n3