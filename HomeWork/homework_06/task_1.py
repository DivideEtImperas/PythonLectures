# Решение с помощью lambda функций

a=int(input('Введите число: '))

days_week = lambda a: f"Выходной"  if a == 6 or a == 7 \
else f"В неделе 7 дней" if a > 7 or a <=0 \
                             else (f"Будни")
print(days_week(a))