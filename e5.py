import sys

a = 0
for i in range(20, sys.maxsize, 20):
    for j in range(1, 21):
        if (i % j != 0):
            break
    else:
        print(i)
        break