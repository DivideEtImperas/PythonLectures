def sort_data(number,read,write,sor,da,data):
    while True:
        num = number()
        if num == '1':
            print(*da(0, read()), sep='\n')
        elif num == '2':
            print(*da(1, read()), sep='')
        elif num == '3':
            print(*da(2, read()), sep='')
        elif num == '4':
            print(*sor(input('Введите № класса: '), read()), sep='')
        elif num == '5':
            print(*read(), sep='')
        elif num == '6':
            print(*sor(input('Введите фамилию ученика:'), read()), sep='')
        elif num == '7':
            write(data())
        elif num == '8':
            print('До свидания!')
            break