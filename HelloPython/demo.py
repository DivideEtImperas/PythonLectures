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



num = input("Введите вещественное число: ")

string = int(num.partition('.')[2]) # преобразуем в строку и удаляем цифры до запятой
number = int(string) # полученые знаки после запятой преобразуем в целое число

# цикл для подсчета суммы цифр в числе
sum = 0
while (number != 0):
    sum = sum + number % 10
    number = number // 10

print("Сумма цифр после точки равна:", sum)
