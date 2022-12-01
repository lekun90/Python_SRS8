# Функция создания и введения журнала событий и действий.
from os.path import exists
import datetime

def log(some_str, result):
    if not exists('log.txt'):
        # Создем файл log.txt
        with open('log.txt', mode='w', encoding="utf-8") as f:
            f.write('Журнал событий БД сотрудников.' + '\n')

    with open('log.txt', mode='a', encoding="utf-8") as f:
        f.write(f'{some_str} = {result} Время события: {datetime.datetime.now()}' + '\n')