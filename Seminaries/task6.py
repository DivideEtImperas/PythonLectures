# 2 Семинар

# 1. 
#  Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81

# x = int(input())
# for i in range(x):
#    print((-3)**i)

# 2й вариант
n = int(input())
print([(-3)**n for n in range(n)])


 
   