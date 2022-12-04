path = '\\Programming\\PythonLectures\\HelloPython\\file.txt'
f = open(path, 'r')    # Связываем файловую переменную с файлом на диске
data = f.read() + ' '
f.close

numbers = []            # Создаем пустой список

# Цикл который запихивает значения из файла в пустой список numbers
while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
    
# Цикл который выводит кортеж из четных чисел и их квадратов
out = []
for e in numbers:
    if not e % 2:
        out.append((e,e**2))
print(out)