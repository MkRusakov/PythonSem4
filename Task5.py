# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


with open("file1.txt", "r", encoding="utf8") as f:
    data1 = str(f.read())
with open("file2.txt", "r", encoding="utf8") as f:
    data2 = str(f.read())

data11 = data1.split("+")
data22 = data2.split("+")

first = str(data11[0])
first1 = str(data22[0])
result1 = int(first[0]) + int(first1[0])

first = str(data11[1])
first1 = str(data22[1])
result2 = int(first[0]) + int(first1[0])

first = str(data11[2])
first1 = str(data22[2])
result3 = int(first[0]) + int(first1[0])

with open("file_task5.txt", "w", encoding="utf8") as f:
        f.write(f"{result1} x^2 + {result2} x + {result3}")
