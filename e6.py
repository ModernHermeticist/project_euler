a = 0
b = 0

for i in range(1, 101):
    a += i ** 2

for i in range(1, 101):
    b += i
b = b ** 2
print(a)
print(b)
print(b - a)