# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

def number(lines):
    counter = 0
    result = []
    for line in lines:
        counter += 1
        result.append(f"{counter}: {line}")
    return result