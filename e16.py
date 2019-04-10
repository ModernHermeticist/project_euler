num = 2 ** 1000
num = str(num)
a = 0
for i in range(len(num)):
    a += int(num[i])
print(a)