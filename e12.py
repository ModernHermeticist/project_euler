import math
def main():
    numOfDivisors = 0
    num = 1
    triNum = 0
    while True:
        triNum = getTriangleNumber(num)
        numOfDivisors = getNumOfDivisors(triNum)
        if (numOfDivisors > 500):
            break
        else: num += 1
    print(triNum)
    print(numOfDivisors)


def getTriangleNumber(a):
    b = 0
    for i in range(1,a+1):
        b += i
    return b

def getNumOfDivisors(a):
    numOfDivisors = 0
    sqr_a = int(math.sqrt(a))

    for i in range(1, sqr_a+1):
        if (a % i == 0):
            numOfDivisors += 2

    if (sqr_a * sqr_a == a):
        numOfDivisors -= 1

    return numOfDivisors

main()