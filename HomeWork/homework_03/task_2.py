# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 



from random import randint

list = [randint(1,10) for i in range(int(input('Введите размер списка: ')))]
print(list)

list_num = int(round((len(list)+1)/2))
print(list_num)
print(f'произведение пар чисел: ',end='')
for i in range(list_num):
    res = list[i]*list[len(list)-1-i] 
    print(res,end = ',')
    

