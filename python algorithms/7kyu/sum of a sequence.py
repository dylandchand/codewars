# Your task is to write a function which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step.

# If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.

def sequence_sum(begin_number, end_number, step):
    return sum([i for i in range(begin_number, end_number+1, step)])