def powers_of_two(n):
    result = []
    for iteration in range (n+1):
        iteration = 2 ** iteration
        result.append(iteration)
    return result