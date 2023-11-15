'''
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
'''
def tower_builder(n_floors):
    # Create an empty list to store tower floors
    tower = []
    # Loop through each floor from 0 to n_floors-1
    for f in range (n_floors):
        # Calculate the number of stars needed for this floor
        stars = "*" * (f*2 + 1)
        # Calculate the number of spaces needed for this floor
        spaces = " " * (n_floors - f - 1)
        # Create a string for this floor, combining stars and spaces
        floor = spaces + stars + spaces      
        # Add this floor to the tower list
        tower.append(floor)
    # Return the tower list
    return tower