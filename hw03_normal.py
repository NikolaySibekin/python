__author__ = 'Николай Сибекин'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """
    Функция фозращает ряд Фиббоначчи с n-элемента до m-элемента.
    Ряд Фиббоначчи - последовательность чисел, в которой первые два числа равны либо 1 и 1, либо 0 и 1,
    а каждое последующее число равно сумме двух предыдущих чисел.
    """
    fib_row = [1, 1]
    item = 0

    while len(fib_row) < m:
        fib_row.append(fib_row[item] + fib_row[item + 1])
        item += 1
    return fib_row[n - 1:m]

print(fibonacci(3, 15))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def bubble_sort(alist):
    """
    Пузырьковая сортировка делает по списку несколько проходов.
    Она сравнивает стоящие рядом элементы и меняет местами те из них,
    что находятся в неправильном порядке.
    Каждый проход по списку помещает следующее наибольшее значение на его правильную позицию.
    В сущности, каждый элемент “пузырьком” всплывает на своё место.
    """
    for pass_num in range(len(alist) - 1, 0, -1):
        for item in range(pass_num):
            if alist[item] > alist[item + 1]:
                temp = alist[item]
                alist[item] = alist[item + 1]
                alist[item + 1] = temp

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(alist)
print(alist)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(user_function, argument_list):
    result = list()
    for item in argument_list:
        if user_function(item):
            result.append(item)
    return result

number_list = range(-9, 9)
less_than_zero = list(my_filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parallelogram(a1, a2, a3, a4):
    if a1[1] == a4[1] or a2[1] == a3[1] and (abs(a1[0] - a2[0]) == abs(a3[0] - a4[0])):
        return True
    return False

dot_a1 = (1, 1)
dot_a2 = (1, 9)
dot_a3 = (10, 6)
dot_a4 = (10, 1)
print(is_parallelogram(dot_a1, dot_a2, dot_a3, dot_a4))