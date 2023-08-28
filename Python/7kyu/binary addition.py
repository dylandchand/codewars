# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

def add_binary(a,b):
    x = bin(a)
    y = bin(b)
    add_binary = bin(int(x,2) + int(y,2)) 
    return (add_binary[2:])