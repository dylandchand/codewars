'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''
def count(s):
    my_dict = {}
    for i in s:
        my_dict[i] = my_dict.get(i,0) + 1
    return my_dict