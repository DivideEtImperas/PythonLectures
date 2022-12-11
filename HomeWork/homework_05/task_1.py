# 1. 
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 117 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

import random
print(f"\n\t^==^ CASINO CANDIES ^==^")
print('\t========================')
print('- Первый ход определяется жеребьёвкой!')
print('- За один ход можно забрать не более 28 конфет')
print('=================================================')

candies = 117

def take_candies():
  global candies   
  while True:
    get_candy = int(input(f'{get_player} Возьмите не более 28 конфет! '))
    if get_candy > 0 and get_candy < 29 and get_candy <= candies:
      candies-=get_candy
      break          
    else:    
      print('Столько конфет брать нельзя!')  

name1 = str(input('Игрок № 1 введите Ваше имя! '))
name2 = str(input('Игрок № 2 введите Ваше имя! '))
players = [name1,name2]
get_player = random.choice(players)
print(f'Первым ходит {get_player}')
while True:
  if get_player == name1:
    take_candies()
    print(f'Конфет осталось: {candies}')
    get_player = name2
    if candies < 29:
      print(f'Победил {get_player}')
      break
  else:
    take_candies()
    print(f'Конфет осталось: {candies}')
    get_player = name1
    if candies < 29:
      print(f'Победил {get_player}')
      break




  

    


      
  
                          

 
  
  

    