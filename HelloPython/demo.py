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

hero = "Harry"
guide = "Dumbledore"
enemy = "Lord V."
print(hash(hero))
# 6175908009919104006
print(hash(guide))
# -5197671124693729851
## Можно ли создать множество строковых значений?
characters = {hero, guide, enemy}
print(characters)
# {'Lord V.', 'Dumbledore', 'Harry'}
## Можно ли создать множество списков?
team_1 = [hero, guide]
team_2 = [enemy]
teams = {team_1, team_2}
# TypeError: unhashable type: 'list'