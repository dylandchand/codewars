# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

# Create as many "shufflings" as you can!

from itertools import permutations as per
def permutations(s):
    return list(set(["".join(i) for i in per(s)]))