#! This program can keep your passwords encrypted

""" With this program, you can keep all your passwords in safety.

    Commands: help, add, remove, find, change, showall, clear """

import database as data

while True:
    task = str(input("Enter a command here: "))
    if task == 'help':
        print(__doc__)
    elif task == 'add':  # Добавления данных в словарь
        a = input(str("Enter resource: "))
        b = input(str("Enter password: "))
        data.add(a, b)
    elif task == 'remove':  # Удаление данных из словаря
        a = input(str("Enter a key: "))
        data.remove(a)
    elif task == 'find':  # Поиск данных в словаре
        a = input(str("Enter a key:"))
        data.find(a)
    elif task == 'change':  # Изменение данных в словаре
        a = input(str("Enter a key you want to rename: "))
        data.change(a)
    elif task == 'showall':  # Показать все данные в словаре
        data.showall()
    elif task == 'clear':
        data.clear()
    else:
        print("No such command %30s" % task)

