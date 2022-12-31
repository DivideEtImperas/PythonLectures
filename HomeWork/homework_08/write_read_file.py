def write_file(data):
    with open('E:\\Programming\\PythonLectures\\HomeWork\\homework_08\\file.csv', 'a',encoding='windows-1251') as file:
        file.writelines(data)


def read_file():
    with open('E:\\Programming\\PythonLectures\\HomeWork\\homework_08\\file.csv', 'r',encoding='windows-1251') as file:
        return file.readlines()