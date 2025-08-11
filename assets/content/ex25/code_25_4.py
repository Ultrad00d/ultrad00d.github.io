def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return 0
    return 1

# ф-ия нахождения всех простых делителей числа
def prime_dividers(n):
    m = []
    # перебор делителей
    for i in range(2, int(n ** 0.5) + 1):
        # если это делитель
        if n % i == 0:
            # если он — простое число, то сохраняем
            if is_prime(i): m.append(i)
            # если обратный делитель — простое число,
            # то сохраняем его
            if is_prime(n // i): m.append(n // i)
    return m

counter = 0
for x in range(5_400_000, 6_000_000):
    # список всех простых делитей числа
    d = prime_dividers(x)
    # если он не пустой
    if d:
        # то M это сумма мин и макс делителя
        M = min(d) + max(d)
        # если M > 60 000 и строка M равна перевернутой 
        # строке M (это палиндром), то
        if M > 60_000 and str(M) == str(M)[::-1]:
            # счетчик чисел до 5 +1
            counter += 1
            # выводим ответ
            print(x, M)
            # если это пятое число, прекращаем перебор
            if counter == 5: break