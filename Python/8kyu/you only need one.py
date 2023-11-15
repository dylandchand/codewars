'''
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
'''
def check(a, x):
    if x in a:    # check if x is in a
        return True    # return True if found
    else:
        return False    # return False if not found