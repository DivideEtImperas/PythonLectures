# Переменные
# Типы данных 
# int, float, boolean, str, list, None

value = None
print (type(value))
a = 123
b = 1.23
print(type(a)) # выводит на консоль
print(type(b))
s = 'hello world'
s = 'hello "world' # Если в одинарных кавычках двойные кавычки будут учитываться
s = "hello 'world" # и наоборот
value = 1234
print (type(value))
print (value)

s = 'hello world'
s = 'hello "world' # Если в одинарных кавычках двойные кавычки будут учитываться
s = "hello 'world" # и наоборот 

print(s) # вывод строки

# Интерполяция строк
print(a, '-',b, '-', s)
print('{} - {} - {}'.format(a,b,s)) 
print('{1} - {2} - {0}'.format(a,b,s)) #В фигурных скобках значения можно менять местами 
print(f'{a} - {b} - {s}') 

# Логическая переменная
f = True # Или False
print(f)

# Списки

list = [1,2,3]  # list = ['1', '2', '3', 'hello'] можно т.о. объявить список строк
print(list)

# Ввод и вывод данных
# print() - отвечает за ввод данных
# input() - отвечает за ввод данных

print('Введите а')
a = int(input())
print('Введите b')
b = int(input())
print(a, ' + ' , b, ' = ', a + b)

 # Арифметические операции
 # +, -, *, /, //, **
 # **, ун-й -, ун-й +,
 # () Cкобки меняют приоритет 

a = 1.312312123
b = 321
c = a + b
c = round(a * b, 5) # round позволяет вывести число до знака, в данном случае их 5
print(c)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &,|,^
# Кое-что еще: is, is not, in, not in
# get

a = 1 < 4 and 5 > 2
f = 1 > 2 or 4 < 6
print(a)
print(f)

f = [1,2,3,4]
print(f)
print(2 in f)     # Ввыводит True 
print(not 2 in f) # Выводит False

is_odd = not f[0] % 2 
print(is_odd)

# Условные конструкции
# if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

#=======================

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША! ')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - то:)')
else:
    print('Привет, ', username)

#========================

original = 23
inverted = 0
while original != 10:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

#========================

original = 23
inverted = 0
while original != 10:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)

#========================

list = [1,2,3,4,10,5]
for i in list: # можно так for i in 1,2,3,4,5:
    print(i)
r = range(10)
for i in r:
    print(i)


# Ввод и вывод данных
# print() - отвечает за ввод данных
# input() - отвечает за ввод данных

print('Введите а');
a = int(input())
print('Введите b');
b = int(input())
print(a, ' + ' , b, ' = ', a + b)

 # Арифметические операции
 # +, -, *, /, //, **
 # **, 
 # () Cкобки меняют приоритет 

a = 1.312312123
b = 321
c = a + b
c = round(a * b, 5) # round позволяет вывести число до знака, в данном случае их 5
print(c)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &,|,^
# Кое-что еще: is, is not, in, not in
# get

a = 1 < 4 and 5 > 2
f = 1 > 2 or 4 < 6
print(a)
print(f)

f = [1,2,3,4]
print(f)
print(2 in f) # Ввыводит True 
print(not 2 in f) # Выводит False

is_odd = not f[0] % 2 
print(is_odd)

# Условные конструкции
# if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

#=======================

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША! ')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - то:)')
else:
    print('Привет, ', username)

#========================

original = 23
inverted = 0
while original != 10:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

#========================

original = 23
inverted = 0
while original != 10:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)

#========================

list = [1,2,3,4,10,5]
for i in list: # можно так for i in 1,2,3,4,5:
    print(i)
r = range(10)
for i in r:
    print(i)

# Работа с текстом

text = 'съешь ещё этих мягких французских булок'

print(len(text))         # 39
print('ещё' in text)      # True
print(text.isdigit())    # False
print(text.isLower())    # True
print(text.replace('ещё','ЕЩЁ'))

for c in text:
    print(c)

# Списки: введение
# list = list

numbers = [1,2,3,4,5]
print(numbers)           # [1,2,3,4,5]
ran = range(1,6)
print(type())
numbers = list(ran)
print(numbers)           # [1,2,3,4,5]
numbers[0] = 10
print(numbers)           # [10,2,3,4,5]
for i in numbers:
    i*=2
    print(i)             # [20,4,6,8,10]
print(numbers)           # [10,2,3,4,5]

#====================

colors = ['red', 'green', 'blue']

for e in colors:
   print(e)            #red green blue

for e in colors:
   print(e*2)          # redredd greengreen blueblue

colors.append('gray')  # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # del colors[0] # удалить элемент

# Функции
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))