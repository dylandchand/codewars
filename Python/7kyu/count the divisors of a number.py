'''
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.
'''
def divisors(n):
    # initialize count
    divisors = 0
    # iterate over range
    for i in range(1,n//2 + 1):
        # check if n is divisible by i
        if n % i == 0:
            # increment count if divisible
            divisors += 1
    # return count plus 1 (for n itself)
    return divisors + 1