import time
def main():
    start = time.time()
    l = []
    for i in range(1, 10000):
        checkIfAmicable(i, l)
    a = 0
    for i in l:
        a += i
    elapsed = time.time() - start
    print("Solution = {}".format(a))
    print('Runtime =', elapsed, 'seconds')
def sum_of_proper_divisors(n):
    s = 0
    mid = int(n / 2)
    for i in range(1, mid+1):
        if n % i == 0:
            s += i
    return s
def checkIfAmicable(a, l):
    b = sum_of_proper_divisors(a)
    if a == b: return
    if sum_of_proper_divisors(b) == a and a not in l and b not in l:
        l.append(a)
        l.append(b)
main()