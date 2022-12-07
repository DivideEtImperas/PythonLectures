# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# *' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

string = 'абвгд гдежз жзе абв  ыопыпт'
task = 'абв'
strArr = string.split()
print(strArr)
for i in strArr:
    if (i.find(task)) != -1:
        strArr.remove(i)
print(strArr)

# Метод с lambda и List Comprehension

del_st = lambda x, y: " ".join([i for i in x.split() if y not in i])

print(del_st('абвгд гдежз жзе абв  ыопыпт', 'абв'))
