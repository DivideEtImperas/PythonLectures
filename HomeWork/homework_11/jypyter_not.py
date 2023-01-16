#f(x) = sin(x)^2 - cos(x)^2

from sympy import *
from sympy.plotting import plot3d



print ('Дана функция f(x) = sin(x)^2 - cos(x)^2')
x = symbols('x')
print(f'корни уравнения: {solve (sin(x)**2 - cos(x)**2, x)}')
print(f'промежутки, на которых f>0: {solve (sin(x)**2 - cos(x)**2, x)}')
print(f'промежутки, на которых f<0: {solve (sin(x)**2 - cos(x)**2, x)}')
ans = diff(sin(x)**2 - cos(x)**2, x)
print(f'вершина ф-ии: {solve (ans)}')
a = diff(sin(x)**2 - cos(x)**2, x)
print(f'промежутки, на которых ф-я возрастает: {solve (a>0)}')
print(f'промежутки, на которых ф-я убывает: {solve (a<0)}')
print(plot(sin(x)**2 - cos(x)**2))
print(plot3d(sin(x)**2 - cos(x)**2))