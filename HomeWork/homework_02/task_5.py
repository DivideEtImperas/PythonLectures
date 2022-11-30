#5. 
# Реализуйте алгоритм перемешивания списка.

import random

list = []
n = int(input('Введите размер списка: '))
for i in range(n):
    list.append(random.randint(0,10))
print(f'Первичный список: {list}')
random.shuffle(list)
print(f'Перемешаный список: {list}')