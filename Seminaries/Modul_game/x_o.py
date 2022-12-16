from os import system 
system("cls")

# карта позиций
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
 
# Метод печати карты на экран
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
# Искуственный интелект: поиск X и О на победных линиях
def check_line(sum_O,sum_X):

    step = ""
    for line in victories:
        o = 0
        x = 0

        for j in range(0, 3):
            if maps[line[j]] == "O":
                o = o + 1
            if maps[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]
    return step 

# Искуственный интелект: выбор хода
def AI():

    step = ""
    # 1)Если на какой либо из победных линий 2 своих и 0 чужих - ставим маркер
    step = check_line(2,0)

    # 2)Если на какой либо из победных линий 2 чужих и 0 своих - ставим маркер
    if step == "":
        step = check_line(0,2)

    # 3)Если одна фигура своя и 0 чужих - ставим маркер
    if step == "":
        step = check_line(1,0)

    # 4)Центр пуст то занимаем центр 
    if step == "":
        if maps[4] != "X" and maps[0] != "O":
            step = 5

    # 5)Если центр занят, то занимаем первую ячейку
    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1

    return step

# Основная логика игры
def run_game():
    game_over = False
    human = True

    while game_over == False:
        # Показываем карту
        print_maps()

        if human == True:
            symbol = 'X'
            step = int(input('Человек, ваш ход: '))
        else:
            print("Компьютер делает ход: ")
            symbol = 'O'
            step = AI()
        # Если компьютер нашел куда ходить то играем иначе ничья.
        if step != "":
            step_maps(step,symbol) # делаем ход в указанную ячейку
            win = get_result() # определяем победителя
            if win != "":
                game_over = True
            else:
                game_over = False
        else:
            print("Ничья!")
            game_over = True
            win = "Победила Дружба!"
        

        human = not(human)
    print_maps()
    print(win)
    return win

if __name__=='__mAIn__':
    run_game()