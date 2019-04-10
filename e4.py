a = []
biggestPal = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        a.append(i * j)

a.reverse()

for num in a:
    k = str(num)
    for j in range(len(k)):
        if (k[j] != k[len(k)-1-j]):
            break
    else:
        if (num > biggestPal):
            biggestPal = num

print(biggestPal)