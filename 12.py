x = 3
start = input('Напишите game, чтобы начать игру: ')
while start == 'game' and x > 0:
    answer = str(input('Угадай число: '))
    if answer == 'off':
        break
    elif answer == '5':
        print ('Вы выиграли билет на концерт')
        break
    else:
        x -= 1
        print ('Попробуйте еще')