# list = []
# numbers = [23,34,45,56,67]
# fruits = ['Aplle', 'Grape','Peach','Banan','Orange']
# print(fruits)
# fractions = [3.14,2.72,1.41,1.73,17.9]
# values = [3.14, 10, 'Hello world!', False, 'Python is the best']
# fruits[3] = 'Watermelon'
# print(fruits)
# print(fruits[2])
# print(fruits[4])
# print(fruits[0])


numbers = ['-2','-1','0','1','2']
data = open('file.txt', 'a')
data.writelines(numbers)
data.close()