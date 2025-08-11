def f(x, end, command=''):
    if x > end + 2: return 0
    if x == end: return 1

    # будем добавлять команду к command
    # Если последние два символа (вызыванных команды) это не AA, то
    if command[-2:] != 'AA': 
        # вызовем все возможные шаги (включая шаг A)
        return f(x + 5, end, command + 'B') + f(x * 2, end, command + 'C') + \
            f(x - 1, end, command + 'A')
    else:
        # иначе, когда было вызвано две команды A подряд,
        # вызовем только шаги B и C
        return f(x + 5, end, command + 'B') + f(x * 2, end, command + 'C')

print(f(5, 34))