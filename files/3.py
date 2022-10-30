original = input("Введите имя исходного файла:")
target = input("Введите имя целевого файла:")

with open(original, "r") as f, open(target, "w") as d:
    data = f.readlines()
    for i in range(len(data)):
        d.write(f'{i}: {data[i]}')