import math

def main():
    num = 2
    square_root_of_num = 0
    primeNumberCounter = 0
    primeToGet = 10001

    while True:
        square_root_of_num = int(math.sqrt(num))
        if isPrime(num, square_root_of_num):
            primeNumberCounter += 1
        if primeNumberCounter == primeToGet:
            print(num)
            break
        num += 1



def isPrime(num, square_root_of_num):
    for i in range(2, square_root_of_num+1):
        if num % i == 0:
            return False
    else: return True

main()
