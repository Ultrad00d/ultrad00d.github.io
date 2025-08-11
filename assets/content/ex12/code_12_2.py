s = 77 * '1'
while '11' in s:
    if '222' in s:
        s = s.replace('222', '1', 1)
    else:
        s = s.replace('11', '2', 1)
print(s)