# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    count_odd = 0
    for n in seq:
        if (seq.count(n) % 2 == 1):
            count_odd = n
            return count_odd
            