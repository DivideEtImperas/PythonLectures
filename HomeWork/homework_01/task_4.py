# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input())
dict = {1:'x>0 y>0', 2:'x<0 y>0', 3:'x<0 y<0', 4:'x>0 y<0'}
print(dict[n])
