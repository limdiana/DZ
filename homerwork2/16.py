text = input()

if text == "Завтрак":
    print("каша")
    exit(0)

if text == "Обед" or text == "Ужин":
    if input("вы хотите плотно поесть?(да/нет): ") == "да":
        print("плов")
        exit(0)
print("Котлета с пюре")
