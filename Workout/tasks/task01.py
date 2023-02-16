# myName = input("Please enter\nyour name: ")
# myAge = input("Hi {} What about your age: ".format(myName))
# text = 'Hello world, my name is {} and I am {} years old.'.format(myName,myAge)
# print(text)

# print('I am 5\'9" tall')


#userInput = input('Enter 1 or 2: ')

#if userInput == "1":
#    print("Hello World")
#    print("How are you?")
#elif userInput == "2":
#    print("Python Rocks!")
#    print("I love Python")
#else:
#    print("You did not enter a valid number")

#num1 = 12 if userInput == "1" else 13

#(num1)


'''Цикл FOR'''
# Цикл по списку
pets = ['cats', 'dogs', 'rabbits', 'hamsters']

#for myPets in pets:
#   print(myPets)

#for index, myPets in enumerate(pets):
#    print(index, myPets)

# Цикл по словарю

age = {'Eva': 5, 'Artur':8}

#for i,j in age.items():
#    print("Name = {}, Age = {}".format(i, j))

# Цикл по строке

#message = 'Hello'

#for i in message:
#    print(i)

# Числовые последовательноти

#for i in range(1,22,3):
#    print(i)
'''Цикл WHILE'''
''' 
counter = 5
while counter > 0:
    print('Counter = ', counter)
    counter = counter - 1
'''
'''Ключевое слово Break
j = 0
for i in range(5):
    j = j + 2
    print('i = ', i, ', j = ',j)
    if j == 6:
        break
'''

''' Ключевое слово Continue
j = 0
for i in range(5):
    j = j + 2
    print ('\ni = ', i, ', j = ', j)
    if j == 6:
        continue
    print ('I will be skipped over if j=6')
'''
'''TRY/EXCEPT'''

#try:
#    answer = 12/0
#    print(answer)
#except:
#    print("An error occurred")


try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter another number: "))
    answer = userInput1/userInput2
    print("The answer is ", answer)
    myFile = open("missing.txt", 'r')


except ValueError:
    print("Error: You did not enter a number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print("Unknown error: ", e)