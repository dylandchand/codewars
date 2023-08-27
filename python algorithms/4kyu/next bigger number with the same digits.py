# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:
#  12 ==> 21
# 513 ==> 531
# 2017 ==> 2071

def next_bigger(n):
    number = [int(i) for i in str(n)]
    pos = len(number) - 1
    next_biggest = float("inf")
    next_biggest_counter = float("inf")
    
    
    if(len(number) == 1 or number == sorted(number, reverse = True)):
        return - 1
    
    # from the right most-digit, find the first digit, k,  that is smaller than the digit in front of it
    for i in range(len(number) -1, 0, -1):
        if (number[i] > number[i-1]):
            pos -= 1
            break
        pos -= 1
    
    # from k, find the next greatest integer
    for i in range(pos, len(number)):
        if (number[i] > number[pos] and number[i] < next_biggest):
            next_biggest = number[i]
            next_biggest_counter = i
    
    # swap k  and the next greatest integer
    number[pos], number[next_biggest_counter] = number[next_biggest_counter], number[pos]
    
    # sort from k+1 to the end of the list
    number2 = number[pos+1:]
    number2.sort()
    for i in range(len(number2)):
        number[i+pos+1] = number2[i]
    
    number = [str(x) for x in number]
    s = "".join(number)
    
    return int(s)

