# Вычислить число c заданной точностью d
import math

def rounded (d, num):
    count = 0
    d = str(d)
    for i in range(len(d)-1, 0, -1):
        if d[i] == ".":
            break
        else:
            count += 1
    print(round(num, count))

rounded(0.0012, math.pi)