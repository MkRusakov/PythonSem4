# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def function(list):
    newlist = []
    for i in range(0, len(list), +1):
        if list.count(list[i]) == 1:
            newlist.append(list[i])
    print(newlist)

sp = [1,3,3,5,6,2,2,2]
function(sp)