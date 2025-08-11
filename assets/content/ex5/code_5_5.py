def convert(n):
    n7 = ''
    while n > 0:
        n, rem = divmod(n, 7)
        n7 = str(rem) + n7
    return n7
def f(n):
    s = convert(n)
    if n % 2 == 0:
        s = '52' + s + '1'
    else:
        if len(s)  == 1:
            s = s + '15'
        else:
            s = s[-1] + s[1:-1] + s[0] + '15'
    return convert(int(s,7))
for i in range(1,1001):
    if len(f(i)) == 4:
        print(i)