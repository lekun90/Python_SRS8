# Создать справочник организации с возможностью импорта и экспорта данных в нескольких форматах
# В консоли предложить пользователю в каком режиме работает:
# 1) запись данных (ввести данные для записи (ФИО, телефон, должность))
# 2) экспорт данных (получить данные из CSV файла, по ID вывести определенные данные)

from log import log
from create_bd_csv import create_bd_csv
from write import write
from read import read

create_bd_csv()

while(True):
    command = input('Командная строка: ')
    if command.lower() == 'добавить':
        command = write()
        txt = 'ОК!' if command else 'ERROR!'
        log('Создание нового сотрудника', txt)
        print('-' * 10)
    elif command.lower() == 'найти':
        command = read()
        txt = 'ОК!' if command else 'ERROR!'
        log('Поиск сотрудников', txt)
        print('-' * 10)
    elif command.lower() == 'завершить':
        break
    else:
        print('Такой команды нет')
