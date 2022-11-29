# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.   

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math
n = int(input("Enter the number: ")) 
count = 1
for i in range(1,n+1): 
      count *=i
      print(f'{count}',end=',')
     
print(f'\nn! =',math.factorial(i))


