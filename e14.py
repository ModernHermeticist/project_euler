import time
def main():
    start = time.time()
    longestChain = 0
    numberOfIters = 0
    for i in range(1, 1000000):
        #print("Testing: {}".format(i))
        t = GenerateCollatz(i)
        if t > numberOfIters:
            longestChain = i
            numberOfIters = t
    print("Starting Number for longest Collatz Chain: {} || Number of iterations: {}".format(longestChain, numberOfIters))
    end = time.time()
    print(end - start)



def GenerateCollatz(n):
    it = 0
    while n != 1:
        if IsEven(n):
            n /= 2
        else: n = 3 * n + 1
        it += 1
    it += 1
    return it


def IsEven(n):
    if n % 2 == 0:
        return True
    return False


main()