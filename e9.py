import math

a = 1
b = 2
c_squared = 0
c = 0

for i in range(a, 500):
    for j in range(b, 501):
        c_squared = (i ** 2) + (j ** 2)
        c = int(math.sqrt(c_squared))
        if c ** 2 == c_squared and i + j + c == 1000:
            print(c_squared)
            print(c)
            print(i * j * c)