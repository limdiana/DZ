price = int(input("Введите сумму: "))
time = int(input("Введите время: "))

if not (0 < time < 23):
    print("время введено некорректно.")
    exit(-1)

if 8 <= time <= 22:
    if 10 <= time <= 12:
        price /= 2

    elif 20 <= time <= 22:
        price /= 4
else:
    print("Магазин закрыт!!!")
    exit(-1)
print(price)