# 5. 
# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.(Дополнительно)

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibonacci(n):
    if n in [1,2]:
        return 1
    elif n == 0:
        return 0
    else:
      return fibonacci(n-1) + fibonacci(n-2)

def negafibonacci(n: int) -> int:
    return(-1)**(n+1)*fibonacci(n)

def seq_of_fibonacci(n: int) -> list[int]:
    list1 = [negafibonacci(i) for i in range(n+1)][::-1]
    list2 = [fibonacci(i) for i in range(1,n+1)]
    return list1 + list2

n = int(input("Введите число: "))

print(seq_of_fibonacci(n))
   
    