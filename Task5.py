# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


with open("file1.txt", "r", encoding="utf8") as f:
    data1 = str(f.read())
with open("file2.txt", "r", encoding="utf8") as f:
    data2 = str(f.read())

data11 = data1.split("+")
data22 = data2.split("+")

result = ''

for i in range(0, len(data11), +1):
    a, b = str(data11[i]), str(data22[i])
    a, b = a[0], b[0]
    current = int(a) + int(b)
    result += current

print(data11)
print(data22)
