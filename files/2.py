with open("python2.txt", "w") as f:
    f.write(", но у меня не получается.")

with open("python.txt", "r") as f:
    text = f.read()

with open("python2.txt", "r") as f:
    text1 = f.read()

print(text + text1)