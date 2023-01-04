# print("Hello, "+ "world!")
# print([1,2,3] + [4,5,6])
# print((1,2)+(3,4))
# print((1,2)*3)
#
# print("s" in "String")
# print("s" in "string")
# print(3 in [1,2,3])
# print(5 in (1,2,3))
# n = 0
# for n in range(1,20):
#     if n == 5:
#         continue
#     if n ==12:
#         break
#     print(n)
#
# n = 0
# for n in range(200, 100, -1):
#     print(n)

# rng = range(1,100)
#
# print(rng.index(5))
# print(rng.count(100))


# for i in range(10):
#     print(i,end=" ")
#
# print()
#
# for i in range(0,50,5):
#     print(i,end=" ")
#
# print()
#
# for i in range(10,0,-1):
#     print(i,end=" ")

# k = 0
# while k < 10:
#     k +=1
#     print(k)

# k = 0
# while k<17:
#     k+=1
#     if k%5 ==0:
#         continue
#     print(k)

# password = ""
# while not password:
#     pasword = input("Пароль: ")


# list = [1,2,3,4,5,6]
# for i in list:
#     print(i)

# from fractions import Fraction
# a = Fraction(6,14)
# print(a)
# b = Fraction(7,23)
# print(b)
# print(a+b)
#
# print(a*b)
#
# c= a+b
# print(c.numerator)
#
# print(c.denominator)


last_name = input("Введите фамилию: ")
# first_name = input("Введите имя: ")
# middle_name = input("Введите отчество: ")
# birth_name = input("Введите дату рождения: ")
# phone_number = input("Введите номер контакта: ")
# note = input("Введите категорию контакта: ")
# spisok = [last_name, first_name, middle_name, birth_name, phone_number, note]
data = []
with open("E:\\Programming\\PythonLectures\\Workout\\readme.csv","r",encoding="utf-8") as f:
        data = f.read().splitlines()
        data.count('\n')
        print(data)
        for i in data:
            if last_name in i:
                n = i.index()
                print(n)
                data.remove(n)
                with open("E:\\Programming\\PythonLectures\\Workout\\readme.csv", "w", encoding="utf-8") as f:
                      print(data)
                # name = [i]
                # name.clear()
                # print()

                # print(i)
                # print(temp)
        # print(data)
#
# with open("E:\\Programming\\PythonLectures\\Workout\\readme.csv", "r", encoding="utf-8") as f:
#          for line in f:
#           print(line)


#
# for i in range(1,6,2):
#     print(i)

# count = 0
# word = "Hello World!"
# for i in word:
#     if i == "l":
#         count += 1
# print("Count:",count)


# i = 5
# while i <= 15:
#     print(i)
#     i += 2
# бесконечный цикл
# isHasCar = True
#
# while isHasCar:
#     if input("Enter data: ") == "Stop":
#         isHasCar = False

# for i in range(1, 11):
#     if i == 5:
#         break
#
#     if i % 2 == 0:
#         continue
#     print(i)


# for i in "hello":
#     if i == "l":
#         found = True
#         break
# else:
#     found = False
#
# print(found )

# l = [1, 2, 2, 4]
# print(l)
# l.clear()
# print(l)
# # [2, 2, 4]