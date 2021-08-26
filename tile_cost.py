'''
A script to calculate cost of tiles to cover a floor
'''

def tiles():

    w = int(input("Please enter the width of the floor in metres: ")) # input is cast as an int so it can be used in formula
    l = int(input("Please enter the length of the floor in metres: "))
    cost = int(input("Please enter the cost of each tile: "))    # cost per tile
    total = (w*l)*cost # total is the total cost
    return f"The total cost of the tiles would be £{total}"

print(tiles())