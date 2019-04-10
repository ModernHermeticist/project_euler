a = 1

for i in range(100, 0, -1):
    a *= i

a = str(a)
b = 0
for num in a:
    b += int(num)

print(b)