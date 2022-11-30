# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) 
#  
# -2 -1 0 1 2 Позиции: 0,1 -> 2

with open ('file.txt', 'r') as data:
    pos = data.readlines()
pos = list(map(int,pos))

n = int(input('Введите число: '))
list = [i for i in range(-n, n+1)]
count = 1
for elem in pos:
    count *= list[elem]
print(pos)
print(list)
print(count)


   