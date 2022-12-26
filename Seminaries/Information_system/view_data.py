def greeting():
    print('Добро пожаловать в телефонный справочник!')


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    birth_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите категорию контакта: ")
    return[last_name, first_name, middle_name, birth_name, phone_number, note]