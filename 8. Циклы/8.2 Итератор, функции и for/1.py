import math


n = int(input())

nok = math.lcm(90, 220, 888)

for i in range(nok, n + 1, nok):
    if i % 90 == 0 and i % 220 == 0 and i % 888 == 0:
        print(i, end=" ")
