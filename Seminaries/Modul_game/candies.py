import random
from os import system 
system("cls")

print(f"\n\t^==^ CASINO CANDIES ^==^")
print('\t========================')
print('- Первый ход определяется жеребьёвкой!')
print('- За один ход можно забрать не более 28 конфет')
print('=================================================')

candies = 117

def take_candies(get_player):
  global candies   
  while True:
    get_candy = int(input(f'{get_player} Возьмите не более 28 конфет! '))
    if get_candy > 0 and get_candy < 29 and get_candy <= candies:
      candies-=get_candy
      break          
    else:    
      print('Столько конфет брать нельзя!')  

def run_game():
    name1 = str(input('Игрок № 1 введите Ваше имя! '))
    name2 = str(input('Игрок № 2 введите Ваше имя! '))
    players = [name1,name2]
    get_player = random.choice(players)
    print(f'Первым ходит {get_player}')
    while True:
        if get_player == name1:
            take_candies(get_player)
            print(f'Конфет осталось: {candies}')
            get_player = name2
            if candies < 29:
               print(f'Победил {get_player}')
               break
        else:
            take_candies(get_player)
            print(f'Конфет осталось: {candies}')
            get_player = name1
            if candies < 29:
               print(f'Победил {get_player}')
               break   
    return get_player

if __name__=='__main__':
    run_game()

            