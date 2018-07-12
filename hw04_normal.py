__author__ = 'Николай Сибекин'

import random
import re

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

def searchLowerNoRe(word_string):
    step = 0
    max_step = 0
    result = list()
    while max_step < len(word_string):
        if word_string[step].isupper() and word_string[step+1].islower():
            step = step + 1
            max_step = step + 1
            while max_step < len(word_string) and word_string[max_step].islower():
                max_step += 1
            if word_string[step:max_step].islower() and max_step != len(word_string):
                result.append(word_string[step:max_step])
        step += 1
    return result

def searchLowerRe(word_string):
    pattern = r"(?<=[A-Z])[a-z]+(?=[A-Z])" #Шаблон
    # Ищем по паттерну и сохраняем в список
    result = [num.group() for num in re.finditer(pattern, word_string)]
    return result
print("#######Задание-1:######## \n")
print("Исходный список:\n")
print(line)
print("\n#######IS NO RE######## \n")
print(searchLowerNoRe(line))
print("\n#######IS RE######## \n")
print(searchLowerRe(line))

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

def seachUpperNoRe(word_string):
    tic = 0
    end = 1
    low_list = list()
    result = list()
    while tic < len(word_string):
        while word_string[tic:end].islower():
            end +=1
        if word_string[tic:end-1].islower():
            low_list.append([tic, end-1])
        tic = end
        end +=1
    tic = 0
    while tic + 1 < len(low_list):
        if low_list[tic][1] - low_list[tic][0] == 2 and low_list[tic+1][1] - low_list[tic+1][0] == 2:
            result.append(word_string[low_list[tic][1]: low_list[tic+1][0]])
        tic += 1
    return result

def searchUpperRe(word_string):
    pattern = r"(?<=[A-Z][a-z][a-z])([A-Z]+)(?=[a-z][a-z][A-Z])"  # Шаблон
    # Ищем по паттерну и сохраняем в список
    result = [num.group(1) for num in re.finditer(pattern, word_string)]
    return result

print("\n#######Задание-2:######## \n")
print("Исходный список:\n")
print(line_2)
print("\n#######IS NO RE######## \n")
print(seachUpperNoRe(line_2))
print("\n#######IS RE######## \n")
print(searchUpperRe(line_2))

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

print("\n#######Задание-3:######## \n")

#Функция генерирует файл
def numberFile():
    tic = 0 #Счетчик
    while tic < 2500: #Тут ставится ограничение насколько длинное у нас получится число
        num = str(random.randint(0, 9)) #Генерируем случайное число от 0 до 9
        file = open('result_hw04_normal.txt', 'a') #Открываем файл на дозапись, автоматом создается если файла нет по указанному пути
        file.write(num) #Записываем наше случайное число в файл
        file.close() #Закрываем файл
        tic += 1

#Функция которая ищет в строке самую длинную последовательность повторяющихся цифр, возвращает координаты этой последовательность
def patternSearch(input_string):

    max_len = 1 #Переменная которая хранит наибольшую найденую длину
    coordinate = list() #Сюда попадут координаты
    for n in range(0, 9): #Так как цифр у нас не так много, генерим список от 0 до 9, сначала ищем самый длинный 0, и тд.
        pattern = r'%d{%d,%d}' % (n, max_len, 9)  #Формируем шаблон поиска
        search_list = re.finditer(pattern, input_string) #Ищем в строке
        for item in search_list: #Проходим по полученным результатам и сравниваем длины
            if len(item.group()) > max_len:
                max_len = len(item.group())
                coordinate = [item.start(), item.end()]
        return coordinate

numberFile()

file = open('result_hw04_normal', 'r')
string_search = file.read()
file.close()
coord = patternSearch(string_search)

print(string_search[coord[0]:coord[1]])