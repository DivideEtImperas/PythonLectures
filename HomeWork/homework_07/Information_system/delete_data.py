def delete_data(word):
    with open('E:\\Programming\\PythonLectures\\Seminaries\\Information_system\\base.csv', 'r',
              encoding="utf-8") as file:
        line = file.readline()
        if line == word:
            return print(line)


