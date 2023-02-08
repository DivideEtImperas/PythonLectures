# print('Hello world!')

# userAge, userName = 30, 'Peter'

# x = 5
# y = 2
# y = x
# print("x = ", x)
# print("y = ", y)

# '''   Summation +   '''
# res = x + y 
# print(res)   # 7

# '''   Subtraction -   '''
# res = x - y
# print(res)   # 3

# '''   Multiplication *   '''
# res = x * y
# print(res)   # 10

# '''   Division /   '''
# res = x / y
# print(res)   # 2.5

# '''   Integer Division //    '''

# res = x // y
# print(res)   # 2 

# '''   Remainder from division %   '''

# res = x % y
# print(res)   # 1 

# '''   Exponentiation **   '''

# res = x ** y
# print(res)   # 25




# String

# variableName = 'Peter' + ' Lee' 
# print(variableName)
# print(variableName.upper())
# print(variableName.lower())

# brand = 'Apple'

# exchangeRate = 1.235235245

# message = 'The price of this %s laptop is %d USD '\
#           'and the exchange rate is %4.2f USD to 1 EUR'\
#           %(brand, 1299, exchangeRate) 
# print(message)

# message = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR'.format('Apple', 1299, 1.235235245) 

# message = 'Артуру {0:d} лет, Еве {1:d} лет они {2:s}'.format(8,5,"большие")
# print(message)

# Списки 

# listName = []
# listName2 = []
# listName3 = []
# listName.append('Artur')
# listName.append('Eva')
# listName2.append('Eduard')
# listName2.append('Julia')
# # del listName[2]
# print(listName)
# print(listName2)
# listName.extend(listName2)
# print(listName)
# # print(len(listName))
# listName3 = sorted(listName)
# print(listName3)

# userAge = [21, 22, 23, 24, 25]

# Кортежи

# monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May")

# print(monthsOfYear*2)
# print(monthsOfYear + ("Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
# print(len(monthsOfYear))
# del monthsOfYear

# Словари

# userNameAndAge = dict(Peter = 38, John = 51, Alex = 13, Alvin = "Not Available")
# userNameAndAge['John'] = 21
# userNameAndAge['Alvin'] = 32
# print(userNameAndAge['John'])
# print(userNameAndAge['Alvin'])
# del userNameAndAge['Peter']
# print(userNameAndAge)
# myDictionary = {}
# myDictionary['Artur'] = 8
# myDictionary['Eva'] = 5
# print(myDictionary)

# print()
# myDict = {"One":1.35, 2.5:"Two Point Five", 3:"+", 7.9:2}
# myDict[2.5] = 'Two and a Half'
# print(len(myDict))
# print(myDict.items())
# print(myDict.keys())



# string

name = "Alice"
hobby = 'golf'
res = 'o' in hobby
print(res)

sum = name + hobby
mult = name*5
print(sum)  # Строки можно складывать 
print(mult) # и умножать

searchI = 'i' in name # оператор in
print(searchI)

text = "Hello world!"
index = 0
for i in text:   # Перебор по индексу
    if i == 'l':
       
        print(i.upper() + 'OL!')

# Срезы строк
word = 'Hello world!'
firstThree = word[0:8:2]
print(firstThree)

# Переменные в нутри строки

name = 'Alice'
greeting = f'Hello, {name}! How are you doing?'
print(greeting)


calculation = f"5 * 6 = {5 * 6}."
print(calculation)