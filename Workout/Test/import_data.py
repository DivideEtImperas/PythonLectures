def import_data(data, sep=None):
    with open('read.csv', 'w',
              encoding="utf-8") as file:

            file.writerow(["Id","Фамилия","Имя","Отчество","Дата рождения","Телефон","Должность"])
            file.writerow(f"\n")
            # file.write(sep.join(data))
            # file.write(f"\n")
