#2. 
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]
      
n = int(input("Введите натуральное число N: "))
div = []
d = 2
m = n 
while d * d <= n:
        if n % d == 0:
            div.append(d)
            n//=d
        else:
            d += 1
div.append(n) 
print('{} = {}' .format(m, div))


