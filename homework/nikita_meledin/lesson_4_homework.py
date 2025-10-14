my_dict = {
    'tuple': (1, 2.5, True, 'Hi', 1),
    'list': [9, None, False, 'zxc', 7.543],
    'dict': {
        'key_1': 1,
        'key_2': (1, 2, 3),
        'key_3': 2, 'key_4': None,
        'key_5': {'value': False}
    },
    'set': {1, 2, 3, 4, 5}}

print(my_dict)

print(my_dict['tuple'][-1])                        # Вывожу последжний элемент кортежа

my_dict['tuple'] = (1, 2.5, True, 'Hi', 1, False)  # Добавляю элемент в конец кортежа
my_dict['tuple'] = (1, True, 'Hi', 1, False)       # Удаляю 2-ой элемент кортежа
print(my_dict['tuple'])

my_dict['list'].append('1')                        # Добавляю в конец списка еще один элемент
print(my_dict['list'])

my_dict['dict']['i am a tuple'] = 'i am a dict'    # Добавляю новый 'ключ': 'значение'
del my_dict['dict']['key_5']                       # Удаляю элемент
print(my_dict['dict'])

my_dict['set'].add(None)                           # Добавляю новый элемент в множество
print(my_dict['set'])
my_dict['set'].remove(3)                           # Удаляю элемент из множества
print(my_dict['set'])

print(my_dict)