'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
'''

def fake_bin(x):
    return ''.join(['1' if int(y) >= 5 else '0' for y in x])