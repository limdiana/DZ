with open("python.txt", "w") as f:
    f.write("Я гений и стараюсь учить питон")

with open("python.txt", "r") as f:
    text = f.read(7)
    print(text)