# Напишите программу для проверки истинности утверждения 

#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 

#  ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

print('----------------------------')
print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ")
print('----------------------------')
x = y = z = True,False
if (not(x or y or z) == (not x and not y and not z)):
    print('True')
else:
    print('False')