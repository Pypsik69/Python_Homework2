# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input("Введите число N: "))
k = 0
two_power = 1

while two_power <= n:
    print(two_power, end=" ")
    k += 1
    two_power = 2 ** k

