# Функция поиска сотрудника
import pandas as pd
from create_bd_csv import BD_sotrudnik_csv

def read():
    print('Нажатие Enter без ввода значения выведет всех сотрудников')
    print('Введите "ID": ')
    key_word = []
    key_word = list(map(str, input().split()))

    df = pd.read_csv(BD_sotrudnik_csv, sep=',', header=None)
    df = df[1:]     # Удаляем заголовок
    df.columns = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона', 'Должность']

    if len(key_word) == 0:
        print(df)
        return True
    else:
        df_new = df.loc[df['ID'] == key_word[0]]
        if df_new.shape[0]:
            print('Введите какую информацию по сотруднику хотите узнать": ')
            print('1: Фамилия; 2: Имя; 3: Отчество; 4: Номер телефона; 5: Должность')
            key_read = input('Введите значение: ')
            if key_read.lower() == '1':
                print(df_new['Фамилия'])
            elif key_read.lower() == '2':
                print(df_new['Имя'])
            elif key_read.lower() == '2':
                print(df_new['Отчество'])
            elif key_read.lower() == '2':
                print(df_new['Номер телефона'])
            elif key_read.lower() == '2':
                print(df_new['Должность'])
            else:
                print('Такого поля нет')
        else:
            print('Данных с таким ID нет.')
        return True