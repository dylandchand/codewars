# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument

def are_you_playing_banjo(name):   
    first = name[0];
    if first == "r" or first == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"