# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

def sort_array(source_array):
    odds = sorted((x for x in source_array if x % 2 != 0), reverse = True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]
        