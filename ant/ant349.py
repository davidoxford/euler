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
    global xpos, ypos, direction

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
    global xpos, ypos, grid

    grid[xpos][ypos] = 1    # Turn black
    turn('CW')
    move()

#-------------------------------------------------------------------
def onBlack():
    global xpos, ypos, grid

    grid[xpos][ypos] = 0    # Turn white
    turn('CCW')
    move()

#-------------------------------------------------------------------
def reCenter():
    global xpos, ypos, grid
    global rows, cols

    center_x = int(cols/2)
    center_y = int(rows/2)

    delta_x = center_x - xpos
    delta_y = center_y - ypos

    #print('delta_x: ', delta_x)
    #print('delta_y', delta_y)

    #for y in range(rows):
    #    for x in range(cols):
    #        print('grid(',x,',',y,') =', grid[x][y])

    # Initialize a new grid
    newgrid = [ [0 for x in range( cols )] for y in range( rows ) ]

    for y in range(rows):
        for x in range(cols):
            if (x - delta_x) in range(0,cols) and (y - delta_y) in range(0,rows):
                newgrid[x][y] = grid[x - delta_x][y - delta_y]
    #            print('newgrid(',x,',',y,') = grid(',x - delta_x,',',y - delta_y,') =', newgrid[x][y])

    #print('New center: [',center_x,',',center_y,']')

    #print(grid)
    #print(newgrid)

    grid = newgrid
    xpos = center_x
    ypos = center_y

#-------------------------------------------------------------------
print('Initializing...')

# Set playing grid size
rows = 151
cols = 151

total_plays = 1000000
total_plays = 11510
total_plays = 1151000

if total_plays >= 10000:
    phase_one_plays = 10000
    phase_two_plays = total_plays - 10000
else:
    phase_one_plays = total_plays
    phase_two_plays = 0


# Initialize rows x cols grid
# 0 = white, 1 = black
grid = [ [0 for x in range( cols )] for y in range( rows ) ]

# Initialize starting location to upper right corner, facing 1 (of 4, e.g., North)
xpos = int(cols/2)
ypos = int(rows/2)
print('Starting at: [',xpos,',',ypos,']')
direction = 1

total_blacks = 0

minx = xpos
miny = ypos
maxx = xpos
maxy = ypos

cur_play = 0
tenths = int(total_plays / 10)

print('Beginning run...')

for play in range(phase_one_plays):
    if xpos >= cols or xpos < 0 or ypos >= rows or ypos < 0:
        break

    if grid[xpos][ypos] == 0:    # On white
        onWhite()
        total_blacks += 1   # We flipped the square to black
    else:
        onBlack()
        total_blacks -= 1   # We flipped the square to white

    #if xpos > maxx:
    #    maxx = xpos
    #if xpos < minx:
    #    minx = xpos
    #if ypos > maxy:
    #    maxy = ypos
    #if ypos < miny:
    #    miny = ypos

    # Print progress in 10% increments
    cur_play += 1
    #if cur_play % tenths == 0:
    #    pct_done = (cur_play / total_plays) * 100
    #    print(int(pct_done), "%")

reCenter()
cycle_count = 0
for play in range(phase_two_plays):
    cycle_count += 1

    if xpos >= cols or xpos < 0 or ypos >= rows or ypos < 0:
        break

    if grid[xpos][ypos] == 0:    # On white
        onWhite()
        total_blacks += 1   # We flipped the square to black
    else:
        onBlack()
        total_blacks -= 1   # We flipped the square to white

    if cycle_count == 3000:
        cycle_count = 0
        reCenter()

    cur_play += 1

#total_blacks = 0
#for row in range(rows):
#    total_blacks += sum(grid[row])

print('Total blacks: ', total_blacks)
#print('Ending position [', xpos, ',', ypos, ']')
print('Total plays:', cur_play)
#print('X max and min:', maxx, minx)
#print('Y max and min:', maxy, miny)

reCenter()
