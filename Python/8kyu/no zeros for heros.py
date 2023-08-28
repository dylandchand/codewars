# Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

def no_boring_zeros(n):
    if n == 0:
        return 0
    else: 
        n = str(n)
        while n[-1] == "0":
            n = n[:-1]
        return int(n)