# 3. 
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

path = 'E:\\Programming\\PythonLectures\\HomeWork\\homework_04\\file_task3.txt'

f = open(path, 'r')
data = f.read() + ' '
f.close()
seq_of_number = []
while data != '':
    pos = data.index(' ')
    seq_of_number.append(int(data[:pos]))
    data = data[pos+1:]
    uniq = [i for i in seq_of_number if seq_of_number.count(i) == 1]
print()
print(f'Исходный список = {seq_of_number}')
print('------------------------------------------------')
print(f'Уникальный список = {uniq}')