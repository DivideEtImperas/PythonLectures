def import_data(data,sep=None):
    with open('E:\\Programming\\PythonLectures\\HomeWork\\homework_07\\base.csv','a+',encoding="utf-8") as file:
        if sep==None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")

