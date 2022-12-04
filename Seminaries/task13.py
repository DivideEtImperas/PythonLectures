#3. 
# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Пример: 
# 4, 5 -> 20
# 7,10 -> 70

x = int(input("Введите число a = "))
y = int(input("Введите число b = "))
def calculate_lcm(x, y): 
    if x > y: 
        greater = x 
    else: 
        greater = y 
    while(True): 
        if((greater % x == 0) and (greater % y == 0)): 
            lcm = greater 
            break 
        greater += 1 
    return lcm 
print(calculate_lcm(x,y))
    