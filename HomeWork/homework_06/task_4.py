# Напишите программу, которая найдёт произведение пар чисел списка. 
import math
list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print('Исходный список: ',list_a)
print('Результат: ',list([a*b for a,b in \
    zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))