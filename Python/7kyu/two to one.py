'''
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
'''
def longest(a1, a2):
    # Sort the merged array
    merged_array = sorted([i for i in set(a1 + a2)])

    # Return the longest subsequence
    return "".join(merged_array)
    