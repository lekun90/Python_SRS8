# Функция создания новой телефонной книги если она отсутствует
from os.path import exists
import csv

BD_sotrudnik_csv = 'BD_sotrudnik.csv'

def create_bd_csv():
    name_header = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона', 'Должность']
    if not exists(BD_sotrudnik_csv):
        with open(BD_sotrudnik_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Создем заголовок таблицы для Phonebook.csv
            writer.writerow(name_header)