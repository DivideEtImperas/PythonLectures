# a = float(input())
# b = float(input())
# print(a,b,sep='\t',end='\r\n')
# x = 0
# while x < 5:
#     print(x)
#     x += 1
# print('Hello world')


# for x in range (1,10): print(x)

# name = input("Как тебя зовут?\n")
# print("Привет, ", name)

# Вывод списка квадратов
# squares = []
# for i in range(10):
#     squares.append(i**2)
# print(squares)

# Вывод списка квадратов одностроковым кодом

# print([i**2 for i in range(10)])


# Строки

# y = "   This is lazy\t\n   "

# print(y.strip())

# print("DrDre".lower())

# print("attention".upper())

# print("smartphone".startswith("smart"))

# print("smartphone".endswith("phone"))

# print("another".find("other"))

# print("cheat".replace("ch", "m"))

# print(','.join(["F", "B", "I"]))

# print(len("Rumplestiltskin"))

# print("ear" in "earth")

# l = [1, 2, 2]
# l.append(4)
# print(l)

# l.insert(2,3)
# print(l)

# print([1,2,2] + [4])

# # l.extend(2, 3)
# # print(l)

# l.remove(1)
# print(l)


# l.reverse()
# print(l)

# l.sort()
# print(l)

# n = int(input('Ваше число сэр: '))
# if n > 3:
#     print("Big")
# elif n == 3:
#     print("Medium")
# else:
#     print("Small")


# # Объявлениие цикла for
# for i in [0,1,2]:
#     print(i)

# # Цикл while - аналогичная семантика
# j = 0
# while j < 3:
#     print(j)
#     j = j+1

# while True:
#     break # цикл не бесконечный

# print("hello world")

# def appreciate(x, percentage):
#     return x + x * percentage / 100

# print(appreciate(10000, 5))


# print((lambda x: x + 3)(3))


# n = float(input('Введите вещественное число:'))


# person1_weight = 121.25
# print(type(person1_weight))


# import random
 
 
# PlayerOne = "Анна"
# PlayerTwo = "Алекс"
 
# AnnaScore = 0
# AlexScore = 0
 
# # У каждого кубика шесть возможных значений
# diceOne = [1, 2, 3, 4, 5, 6]
# diceTwo = [1, 2, 3, 4, 5, 6]
 
# def playDiceGame():
#     """Оба участника, Анна и Алекс, бросают кубик, используя метод shuffle"""
 
#     for i in range(5):
#         #оба кубика встряхиваются 5 раз
#         random.shuffle(diceOne)
#         random.shuffle(diceTwo)
#     firstNumber = random.choice(diceOne) # использование метода choice для выбора случайного значения
#     SecondNumber = random.choice(diceTwo)
#     return firstNumber + SecondNumber
 
# print("Игра в кости использует модуль random\n")
 
# #Давайте сыграем в кости три раза
# for i in range(3):
#     # определим, кто будет бросать кости первым
#     AlexTossNumber = random.randint(1, 100) # генерация случайного числа от 1 до 100, включая 100
#     AnnaTossNumber = random.randrange(1, 101, 1) # генерация случайного числа от 1 до 100, не включая 101
 
#     if( AlexTossNumber > AnnaTossNumber):
#         print("Алекс выиграл жеребьевку.")
#         AlexScore = playDiceGame()
#         AnnaScore = playDiceGame()
#     else:
#         print("Анна выиграла жеребьевку.")
#         AnnaScore = playDiceGame()
#         AlexScore = playDiceGame()
 
#     if(AlexScore > AnnaScore):
#         print ("Алекс выиграл игру в кости. Финальный счет Алекса:", AlexScore, "Финальный счет Анны:", AnnaScore, "\n")
#     else:
#         print("Анна выиграла игру в кости. Финальный счет Анны:", AnnaScore, "Финальный счет Алекса:", AlexScore, "\n")

# # Игра КОНФЕТЫ
# # вариант человек против бота:
# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = randint(1,29)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


# Рандомайзер символов
from random import randint

collection = [randint(100, 7000) for i in range(10)]

def my_func(var: int):
    print(chr(var), end=' ')

set(map(my_func, collection))