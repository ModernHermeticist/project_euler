import math


for n in range(1, 1001):
    frac, whole = math.modf(1/n)


    frac = str(frac).split('.')[1]
    print(frac)