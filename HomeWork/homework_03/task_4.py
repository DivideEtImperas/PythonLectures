# 4. 
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec_number= int(input('Введите десятичное число: '))
bin_number = int(bin(dec_number)[2:])
print(f'{dec_number} = {bin_number}')