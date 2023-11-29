'''
Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
'''
import math
def round_to_next5(n):
    return (math.ceil(n / 5) * 5)