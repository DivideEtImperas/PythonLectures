from datetime import datetime as dt
from time import time

def game_logger(data):
    time = dt.now().strftime('%H:%M:%S')
    with open('E:\\Programming\\PythonLectures\\Seminaries\\Modul_game\\log.txt', 'w',encoding="utf-8") as file:
        file.write('\n{} Победитель - {}'.format(time, data))