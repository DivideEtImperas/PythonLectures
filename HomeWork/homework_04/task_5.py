# 5. 
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9


from sympy import simplify
# Путь первого полинома
path = 'E:\\Programming\\PythonLectures\\HomeWork\\homework_04\\file1_task5.txt'

file1_task5 = open(path, 'r')
data1 = file1_task5.read()
print(f'Первый многочлен: {data1} ')
file1_task5.close()

# Путь второго полинома
path = 'E:\\Programming\\PythonLectures\\HomeWork\\homework_04\\file2_task5.txt'

file2_task5 = open(path, 'r')
data2 = file2_task5.read()
print(f'Второй многочлен: {data2} ')
file2_task5.close()

sum_pol= simplify(data1 + '+' + data2)
sum_pol = str(sum_pol)

print(f'Сумма многочленов: {sum_pol}')

sum_data_pol = 'file_sum_task5'
with open(f'E:\\Programming\\PythonLectures\\HomeWork\\homework_04\\{sum_data_pol}.txt', 'w') as s:
   s.write(sum_pol)
