# Ф-ция ввода нового контакта в телефонную книгу.
# Формат ввода: Фамилия, Имя, Телефон, Описание.

import re
import csv
from create_bd_csv import BD_sotrudnik_csv

def write():
    print('Введите через пробел: ID, Фамилию, Имя, Отчество, Телефон, Должность:')
    new_str = list(map(str, input().split()))

    if len(new_str) != 6:
        print('Ошибка: нужно заполнить 6 полей: ID, Фамилию, Имя, Отчество, Телефон, Должность.')
        return False
    else:
        with open(BD_sotrudnik_csv, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Создем заголовок таблицы для BD_sotrudnik_csv.csv
            writer.writerow(new_str)
        return True