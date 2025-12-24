import datetime

my_date = 'Jan 15, 2023 - 12:05:33'
print(f'Полученная дата: {my_date}')
my_date_py = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
print(f'Дата в python формате: {my_date_py}')
month = my_date_py.strftime('%B')
print(f'Месяц: {month}')
date_new_format = datetime.datetime.strftime(my_date_py, '%d.%m.%Y, %H:%M')
print(f'Дата в новом формате: {date_new_format}')
