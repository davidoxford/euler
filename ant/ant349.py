def move(xpos, ypos, direction):
    next_x = xpos
    next_y = ypos
    if direction == 1:
        next_y -= 1
    elif direction == 2:
        next_x += 1
    elif direction == 3:
        next_y += 1
    else: # direction == 4:
        next_x -= 1

    return [next_x, next_y]
#-------------------------------------------------------------------
def turn(direction, whichway):
    if whichway == 'CW':
        if direction != 4:
            return direction + 1
        else:
            return 1
    else:  # Turn CCW
        if direction != 1:
            return direction - 1
        else:
            return 4

#-------------------------------------------------------------------
def onWhite(xpos, ypos, direction):
    grid[xpos][ypos] = 1    # Turn black
    turn(direction)

#-------------------------------------------------------------------

# Initialize 100 x 100 grid
# 0 = white, 1 = black
grid = [ [0 for x in range( 10 )] for y in range( 10 ) ]

# Initialize starting location to approx center of grid, facing 1 (of 4, e.g., North)
xpos = 5
ypos = 5
direction = 1

for play in range(5):
    if grid[xpos][ypos] = 0:    # On white
