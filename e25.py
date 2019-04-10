def main():
    n_1 = 1
    n_2 = 0
    n = 0
    i = 2
    while True:
        n = n_1 + n_2
        sn = str(n)
        if len(sn) == 1000:
            print("Fibonacci Index {} is {}".format(i, sn))
            break
        n_2 = n_1
        n_1 = n
        i += 1


main()
