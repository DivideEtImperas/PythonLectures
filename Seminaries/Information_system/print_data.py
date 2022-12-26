def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15), "Категория".center(30))
    else:
        print("Справочник пуст!")