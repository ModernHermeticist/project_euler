import math

largestprimefactoG = 0

def main():
    n = 600851475143
    a = int(math.sqrt(n))
    largestprimefactor(n, a)
    print("Largest Prime Factor of {}: {}".format(n, largestprimefactoG))



def largestprimefactor(n, a):
    global largestprimefactoG
    if (n <= 1):
        return
    for i in range(2, a+1):
        if (n % i == 0 and i > largestprimefactoG):
            for j in range(2, int(math.sqrt(i)+1)):
                if (i % j == 0):
                    return
            largestprimefactor(i, int(math.sqrt(i)))
            largestprimefactoG = i






main()