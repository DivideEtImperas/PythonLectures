print("*" * 15, " Калькулятор ", "*" * 10)
print("Для выхода введите q в качестве знака операции")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == 'q': break
    if s in ('+','-','*','/'):
        x = float(input("value x="))
        y = float(input("value y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
          if y !=0:
            print("%.2f" % (x/y))
          else:
            print("На ноль делить нельзя!")
    else:
        print("Неверный знак операции!")