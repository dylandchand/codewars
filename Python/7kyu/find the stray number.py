'''
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.
'''
def stray(arr):
    # Returns the first occurrence of an element that occurs only once in the list.
    for i in arr:
        # If an element occurs only once, return it
        if arr.count(i) == 1:
            return i

