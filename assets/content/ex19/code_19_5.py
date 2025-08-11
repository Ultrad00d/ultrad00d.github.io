def f(s, m):
    # усл. победы — камней <= 19
    if s <= 19: return m % 2 == 0
    if m == 0: return 0
    # действие 1)
    h = [f(s - 5, m - 1)]
    # условие 2)
    if s % 2 == 0: h.append(f(s // 2, m - 1))
    # условие 3)
    elif s % 3 == 0: h.append(f(s // 3, m - 1))
    # условие 4)
    else: h.append(f(s + 1, m - 1))
    
    return any(h) if m % 2 == 1 else all(h)