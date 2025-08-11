from fnmatch import fnmatch

# оптимально перебираем числа
for x in range(2024, 10 ** 10 + 1, 2024):
    # смотрим чтобы они подходили под маску
    if fnmatch(str(x), '1?2157*4'):
        # выписываем ответ
        print(x, x // 2024)