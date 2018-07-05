__author__ = 'Николай Сибекин'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruit = ["яблоко", "банан", "киви", "арбуз"]
print("Дано: ", fruit)

print("Вывод: ")
for item in fruit:
    num = fruit.index(item) + 1
    print(str(num) + "." + '{:>7}'.format(item))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok_1 = ["Анна", "Петя", "Вася", "Даша", "Маша", "Света"]
spisok_2 = ["Петя", "Костя", "Юра", "Вася"]

print("\nИсходные данные")
print("Список 1: ", spisok_1)
print("Список 2: ", spisok_2)

for item_2 in spisok_2:
    for item_1 in spisok_1:
        if item_2 == item_1:
            spisok_1.remove(item_2)

print("\nПосле удаления")
print("Список 1: ", spisok_1)
print("Список 2: ", spisok_2)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = [4, 5, 8, 23, 67, 24]
print("\nСтарый список: ", numbers)

numbers_new = []

for number in numbers:
    if number %2 == 0:
        numbers_new.append(int(number/4))
    else:
        numbers_new.append(number*2)

print("Новый список:  ", numbers_new)


