import os
from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
homework = os.path.dirname(os.path.realpath(base_path))
homework_file_path = os.path.join(homework, 'eugene_okulik/hw_13', 'data.txt')


with open(homework_file_path, 'r') as file:
    for line in file:
        section = line.split()
        date_str = f'{section[1]} {section[2]}'
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

        index = section[0].replace('.', '')

        if index == '1':
            print(f'Дата на неделю позже: {date_obj + timedelta(weeks=1)}')
        elif index == '2':
            print(f'Какой день недели: {date_obj.strftime("%A")}')
        elif index == '3':
            diff = datetime.now() - date_obj
            print(f'Сколько дней назад была эта дата: {diff.days}')
