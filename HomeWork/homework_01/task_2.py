# Напишите программу для проверки истинности утверждения 

#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 

#  ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"


X = Y = Z = True,False
if (not(X or Y or Z) == (not X and not Y and not Z)):
    print('True')
else:
    print('False')