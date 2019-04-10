import math
def main():
    a = 0
    upperbound = 2000000
    for i in range(2, upperbound):
        square_root_i = int(math.sqrt(i))
        if isPrime(i, square_root_i):
            a += i

    print(a)


def isPrime(num, square_root_of_num):
    for i in range(2, square_root_of_num+1):
        if num % i == 0:
            return False
    else: return True


main()