# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random


def function(k):
    list = []
    for i in range(0, k+1, +1):
        list.append(random.randint(0, 99))
    # result = list[0], 'x^2 +', list[1], 'x + ', list[2], ' = 0'
    with open("file_task4.txt", "w", encoding="utf8") as f:
        f.write(f"{str(list[0])} x^2 + {str(list[1])} x +  {str(list[2])}  = 0")
function(2)