def main():
    a = 0
    i = 1
    b = 0
    while a <= 4000000:
        a = fib(i)
        print("Fib of {}: {}".format(i, a))
        i += 1
        if (a % 2 == 0):
            b += a

    print("The sum is {}".format(b))


def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-1) + fib(num-2)


main()