"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import threading
import time

def inputik():
    a = 0
    while True:
        message = input("What do you want to be reminded of? ")
        seconds = int(input("How many seconds from now should I remind you? "))
        time.sleep(seconds)
        print(message)
        a += 1
        if a == 3:
            print("Reminder limit reached.")
            break

def bomba():
    parol = input("\nEnter the code: ")
    if parol == "baldez":
        print("Bomb defused.")
    else:
        print("Bomb exploded.")

if __name__ == "__main__":
    thread = threading.Thread(target=inputik)
    thread.daemon = True
    thread.start()
    bomba()