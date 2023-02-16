#friend = 'Максим'

#first_letter = friend[0]
#print('Первая буква имени друга', first_letter)

#name = 'Эдуард Голышев 32'
#print(name)

#print(len(name))

#print(name.find('Гол'))

#print(name.split())
#print(name.split(';'))

#print(name.isdigit())

#print(name.upper())
#print(name.lower())


#name = 'Leo'
#age = 30
#1. Конкатенация
'''hello_str = 'Привет, ' + name + ' тебе ' + str(age) + ' лет'
print(hello_str)
#2. %
hello_str = 'Привет %s тебе %d  лет'% (name, age)
print(hello_str)
#3. format
hello_str = 'Привет {} тебе {} лет'.format(name, age)
print(hello_str)'''
'''
users = int(input('Введите кол-во участников: '))
res_list = []
while users != 0:
   name = input('Кто занял {} место?: '.format(users))
   users -= 1
   res_list.append(name)
print(f"В соревновании участвовали: ", res_list )

# можно объявить  пыустой список
empty_list = []

# можно объявить список и сразу заполнить его эл-ми
friends = ['Max' , 'Leo', 'Kate']

# тип списка - list
print(type(friends))  # <class 'list'>

# как и встроке для списка доступны индексы(начиная с 0)
print('Второй друг: ', friends[1])
print('Первый друг c конца: ', friends[-1])

# так же можно применить срезы
print(friends[1:2])  # ['Max' , 'Leo', 'Kate']
print(friends[:2])   # ['Max' , 'Leo']
print(friends[1:])   # ['Leo', 'Kate']
'''
'''
print('* Соревнования по Python *')
count = int(input('Введите кол-во участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место '.format(i))
    members.append(name)
    i-=1
print(members)
# Кто участвовал в соревновании по алфавиту
print('В соревновании участвовали: ',sorted( members))

# Мы записали людей с конца?
members.reverse()


# Нам нужно взять певые 3 места
result = members[:3]

result = 'Победители: {}. Поздравляем!'.format(result)
print(result)
'''




winners = ['Max', 'Leo', 'Kate']

# простой перебор
for winner in winners:
    print(winner)

# используем range
for i in range(len(winners)):
    # print(i)
    print(i+1,')', winners[i])


numbers = [1,3,5]

for number in numbers:
    print(number)

print(list(range(1,10,2)))
