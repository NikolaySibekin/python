__author__ = 'Николай Сибекин'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    """
    Функция кругляет произвольное десятичное число (number) до количества знаков,
    переданных вторым агрументом (ndigits)
    """
    fraction = number % 1 * (10 ** ndigits)  # получаем число до нужного знака
    rem = fraction % 1  # смотрим какие числа остались
    if rem * 2 >= 1:
        rem = 1
    else:
        rem = 0
    # собирем округленное число
    fraction = fraction // 1 + rem
    number = str(int(number // 1)) + ('.' + str((fraction / (10 ** ndigits)))[2:])
    return float(number)

print(my_round(6.123456789, 6))
print(my_round(6.123456789, 3))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    """Функция определят, является ли билет счастливым"""
    left_number = 0
    right_number = 0

    for item_left in str(ticket_number // 1000):
        left_number += int(item_left)

    for item_right in str(ticket_number % 1000):
        right_number += int(item_right)

    if left_number != right_number:
        return False
    else:
        return True

print(lucky_ticket(234182))
print(lucky_ticket(123006))
