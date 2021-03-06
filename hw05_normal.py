__author__ = 'Николай Сибекин'

import sys
import os
 
# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"
 
# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл из easy.py
 
# user_input
ui = input('Выберите действие:\n1 - Перейти в папку;\n2 - Просмотреть содержимое текущей папки;'
               '\n3 - Удалить папку;\n4 - Создать папку;\n''q'' для выхода из программы\n')
 
def dir_util(ui):
"""
Работа с папками текущей директории (переход, просмотр, создание, удаление)
"""
# user_input
    ui = input('Выберите действие:\n1 - Перейти в папку;\n2 - Просмотреть содержимое текущей папки;\n3 - Удалить папку;\n4 - Создать папку;\n''q'' для выхода из программы\n')
    
    if ui == '1':
        ui_dir = input('Введите путь нужной директории')
        os.chdir(ui_dir)
        try:
            cwd = os.getcwd()
            print('Вы успешно перешли в ', cwd)
        except(FileNotFoundError, OSError):
            print('Не верно указан путь: ', ui_dir)
    elif ui == '2':
        from hw05_easy import dir_contains as ch2
        ch2()
    elif ui == '3':
        from hw05_easy import path_remove as ch3
        ch3(path_to_remove = input('Какую папку удаляем?'))
    elif ui == '4':
        from hw05_easy import new_path as ch4
        ch4(name = input('Введите название новой папки'))

dir_util(ui)