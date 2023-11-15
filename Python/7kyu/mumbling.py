'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
def accum(s):
    # initialize an empty list to store output
    output = []
    
    # iterate over the string using enumerate
    for count, letter in enumerate(s):
        # append the transformed letter to the output list
        output.append(letter.upper() + letter.lower() * (count))
    
    # return the output list as a string joined by hyphens
    return '-'.join(output)