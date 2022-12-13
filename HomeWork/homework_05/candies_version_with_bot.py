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
print('\t=========================')
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

def bot_player():
  global candies
  while True:
    bot_get_candy = random.randint(1,28)
    print(f'{bot} взял {bot_get_candy} конфет')
    if bot_get_candy > 0 and bot_get_candy < 29 and bot_get_candy <= candies:
      candies-=bot_get_candy
      break


name1 = str(input('Введите Ваше имя! '))
bot = 'Computer'
players = [name1,bot]
get_player = random.choice(players)
print(f'Первым ходит {get_player}')
while True:
  if get_player == name1:
    take_candies()
    print(f'Конфет осталось: {candies}')
    get_player = bot
    if candies < 29:
      print(f'Победил {get_player}')
      break
  else:
    bot_player()
    print(f'Конфет осталось: {candies}')
    get_player = name1
    if candies < 29:
      print(f'Победил {get_player}')
      break
