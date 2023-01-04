import csv

with open("E:\\Programming\\PythonLectures\\Workout\\Test\\readme.csv",mode="w", encoding='utf-8') as f:

     file_writer = csv.writer(f, delimiter = "|", lineterminator="\r")
     file_writer.writerow(["ID","Фамилия", "Имя", "Отчество", "Дата рождения", "Телефон", "Должность"])



