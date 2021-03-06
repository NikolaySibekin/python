__author__ = 'Николай Сибекин'

import classes as cl

#Правила игры "Лото"
#Игра ведется с помощью специальных карточек, на которых отмечены числа, и фишек (бочонков) с цифрами.

#Количество бочонков — 90 штук (с цифрами от 1 до 90).

#Каждая карточка содержит 3 строки по 9 клеток.
#В каждой строке по 5 случайных цифр, расположенных по возрастанию.
#Все цифры в карточке уникальны.

#В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается случайная карточка.

#Каждый ход выбирается один случайный бочонок и выводится на экран.
#Также выводятся карточка игрока и карточка компьютера.

#Пользователю предлагается зачеркнуть цифру на карточке или продолжить.

#Если игрок выбрал "зачеркнуть":
#Если цифра есть на карточке - она зачеркивается и игра продолжается.
#Если цифры на карточке нет - игрок проигрывает и игра завершается.

#Если игрок выбрал "продолжить": Если цифра есть на карточке - игрок проигрывает и игра завершается.
#Если цифры на карточке нет - игра продолжается.

#Побеждает тот, кто первый закроет все числа на своей карточке.


def main():
    user_answer = True
    while user_answer:
        match = cl.Game()

        input_data = input("\nЕщё партию?\n(Y/N): ")
        if input_data != "Y" and input_data != "y":
            user_answer = False

if __name__ == "__main__":
    main()