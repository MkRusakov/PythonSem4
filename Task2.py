# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def function(N):
    result = []
    d = 2
    while d**2 <= N:
        if N % d == 0:
            result.append(d)
            N = N // d
        else:
            d += 1
    result.append(N)
    print(result)
function(36)
