#1. 
# Вычислить число Пи c заданной точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

import math

def toFixed(x: float, n=0):
    a, b = str(x).split('.')
    return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))
x = math.pi
numberzeros = int(input("Укажите кол-во знаков после запятой для числа π: "))
if numberzeros != 0:
   print(toFixed(x,numberzeros))

