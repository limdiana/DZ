"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import threading
import time

def remind():
    message = input("What do you want to be reminded of? ")
    seconds = int(input("How many seconds from now should I remind you? "))
    time.sleep(seconds)
    print(message)

reminder_thread = threading.Thread(target=remind)
reminder_thread.start()

time.sleep(10)
print("Program is exiting")
