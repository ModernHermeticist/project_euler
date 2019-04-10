# A number n is called deficient if the sum of its proper divisors is less than n
# It is called abundant if this sum exceeds n.
# It is called perfect if this sum equals n.

# 12 is the smallest abundant number
# 24 is smallest number that can be written as the sum of two abundant numbers
# All integers greater than 28123 can be written as the sum of two abundant numbers
# This upper limit cannot be reduced by analysis though it is known that the greatest 
# number that cannot be expressed as the sum of two abundant numbers is less than this limit

# Find the sum of all positive numbers which cannot be written as the sum of two abundant numbers

# First generate sums of divisors




def main():
    abundantNumbers = []
    for n in range(1, 28124):
        sum = GenerateSumOfDivisors(n)
        if sum > n:
            abundantNumbers.append(n)
    print(len(abundantNumbers))
    print(abundantNumbers[len(abundantNumbers)-1])



def GenerateSumOfDivisors(n):
    sum = 0
    for i in range(1, int(n/2 + 1)):
        if n % i == 0:
            sum += i
    return sum


main()