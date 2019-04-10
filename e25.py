def main():
    for n in range(0, 11):
        print(fibonacci(n))


def fibonacci(n):
    if n == 0:
        return 0
    if n < 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

main()