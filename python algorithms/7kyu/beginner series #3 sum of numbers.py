# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.
# Note: a and b are not ordered!

def get_sum(a,b):
    return sum(list(range(a,b + 1))) if a < b else sum(list(range(b,a + 1)))