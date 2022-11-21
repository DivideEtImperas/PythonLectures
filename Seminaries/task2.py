# Напишите программу, которая принимает на вход два числа и проверяет
# является ли одно число квадратом другого.


# a = int(input())
# b = int(input())

# if a == b**2 or a**2 == b:
#     print(f'Является')
# else:
#     print(f'Не является')
 
# if a == b**2:
#     print('{a} квадрат {b}')
# elif b == a**2:
#     print('{b} квадрат {a}')
# else:
#     print('NO')
# print((a == b**2) or (b == a**2)) 

# Напишите програму,
# которая на вход принимает 5 чисел и находит максимальное из них


# max = int(input())

# for i in range(4):
#     b = int(input())
#     if b > max:
#         max = b
# print(max) 


a = input().split(',')
print(a)

# или так 

a = list(map(int, input().split()))
print(max(a))
