#2. 
# Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)

# карта позиций
from os import system 
system("cls")
maps = [1,2,3,
        4,5,6,
        7,8,9]
# Выигрышные позиции 
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
# Мето печати карты на экран
def print_maps():
    print()
    print(maps[0], end = " | ")
    print(maps[1], end = " | ")
    print(maps[2])
    print('--|---|--')
    print(maps[3], end = " | ")
    print(maps[4], end = " | ")
    print(maps[5])
    print('--|---|--')
    print(maps[6], end = " | ")
    print(maps[7], end = " | ")
    print(maps[8])
# Выбор позиции на карте
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol

def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
            win = 'X'
        if maps[i[0]] == 'O' and maps[i[1]] == 'O' and maps[i[2]] == 'O':
            win = 'O'

    return win
# Основной алгоритм
game_over = False
player1 = True

while game_over == False:
    print_maps()
    # Спрашиваем у играющего куда делать ход
    if player1 == True:
        symbol = 'X'
        step = int(input('Игрок 1, Ваш ход! '))
    else:
        symbol = 'O'
        step = int(input('Игрок 2, Ваш ход! '))
    
    step_maps(step,symbol) # Ход в указанную позицию
    win = get_result() # Определяем победителя
    if win != '':
        game_over = True
    else:
        game_over = False

    player1 = not(player1)

# Игра окончена. Показываем карту. Объявляем победителя
print_maps()
print('Победил',win)