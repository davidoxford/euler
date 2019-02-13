#-------------------------------------------------------------------
# David Oxford - 2/9/2019
# https://github.com/davidoxford/euler/tree/master/ant
#
#-------------------------------------------------------------------
# Project Euler Problem 349
# https://projecteuler.net/problem=349
#
# An ant moves on a regular grid of squares that are coloured either black or white.
# The ant is always oriented in one of the cardinal directions (left, right, up or down) and moves from square to adjacent square according to the following rules:
# - if it is on a black square, it flips the colour of the square to white, rotates 90 degrees counterclockwise and moves forward one square.
# - if it is on a white square, it flips the colour of the square to black, rotates 90 degrees clockwise and moves forward one square.
#
# Starting with a grid that is entirely white, how many squares are black after 1018 moves of the ant?
#-------------------------------------------------------------------
#
# Current implementation plays the game with minimal regard to the structure. The ant progress from upper right to
# lower left (if origin is in upper left, y increasing downward), so the starting point is set to near the upper right
# corner. Current implementation allows for ~ 10^6 moves on a 20,000 x 20,000 grids.
#
# Next step will be to account for the repeating structure of the moves and only track the necessary grid data, minimizing
# the size of "grid" and thereby significantly reducing computational complexity, allowing for more moves to be calculated.
#
#-------------------------------------------------------------------

def move():
    global direction
    global xpos
    global ypos

    if direction == 1:
        ypos -= 1
    elif direction == 2:
        xpos += 1
    elif direction == 3:
        ypos += 1
    else: # direction == 4:
        xpos -= 1

#-------------------------------------------------------------------
def turn(whichway):
    global direction

    if whichway == 'CW':
        if direction != 4:
            direction += 1
        else:
            direction = 1
    else:  # Turn CCW
        if direction != 1:
            direction -= 1
        else:
            direction = 4

#-------------------------------------------------------------------
def onWhite():
    global xpos
    global ypos

    grid[xpos][ypos] = 1    # Turn black
    turn('CW')
    move()

#-------------------------------------------------------------------
def onBlack():
    global xpos
    global ypos

    grid[xpos][ypos] = 0    # Turn white
    turn('CCW')
    move()

#-------------------------------------------------------------------
print('Initializing...')

# Set playing grid size
rows = 2000
cols = 2000

total_plays = 1000000
total_plays = 10
# Initialize rows x cols grid
# 0 = white, 1 = black
grid = [ [0 for x in range( cols )] for y in range( rows ) ]

# Initialize starting location to upper right corner, facing 1 (of 4, e.g., North)
xpos = cols - 50
ypos = 50
direction = 1

minx = xpos
miny = ypos
maxx = xpos
maxy = ypos

cur_play = 0
tenths = int(total_plays / 10)

print('Beginning run...')

for play in range(total_plays):
    if xpos >= cols or xpos < 0 or ypos >= rows or ypos < 0:
        break

    if grid[xpos][ypos] == 0:    # On white
        onWhite()
    else:
        onBlack()

    if xpos > maxx:
        maxx = xpos
    if xpos < minx:
        minx = xpos
    if ypos > maxy:
        maxy = ypos
    if ypos < miny:
        miny = ypos

    # Print progress in 10% increments
    cur_play += 1
    #if cur_play % tenths == 0:
    #    pct_done = (cur_play / total_plays) * 100
    #    print(int(pct_done), "%")

total_blacks = 0
for row in range(rows):
    total_blacks += sum(grid[row])

print('Total blacks: ', total_blacks)
print('Ending position [', xpos, ',', ypos, ']')
print('Total plays:', cur_play)
print('X max and min:', maxx, minx)
print('Y max and min:', maxy, miny)
