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
# The problem is approached in two parts. First part (initial 11,000 moves or so) simulates the actual moves made to count
# how many squares are made black.  Somewhere in there, the movement becomes a 104-move cycle, so the second phase is to
# determine how many blacks are added per cycle, and then multiply by the number of cycles to get the remaining additional
# blacks.
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
    # This function is not used in the final implementation of the solution. It was created for an
    # interim solution where the grid "followed" the ant, allowing a much smaller grid to be used.
    # This worked fine, but was still too computationally intensive to solve the given 10^18 problem.

    global xpos, ypos, grid
    global rows, cols

    center_x = cols // 2
    center_y = rows // 2

    delta_x = center_x - xpos
    delta_y = center_y - ypos

    # Initialize a new grid
    newgrid = [ [0 for x in range( cols )] for y in range( rows ) ]

    # Populate new grid with black / white info from the old grid
    for y in range(rows):
        for x in range(cols):
            if (x - delta_x) in range(0,cols) and (y - delta_y) in range(0,rows):
                newgrid[x][y] = grid[x - delta_x][y - delta_y]

    # Implement new grid and place ant back in the center
    grid = newgrid
    xpos = center_x
    ypos = center_y

#-------------------------------------------------------------------

# Set the total number of plays
total_plays = 1000000000000000000

# Set playing grid size
rows = 151
cols = 151

cycle_size = 104    # Number of steps in repeating cycle once the ant takes off, determined through testing
random_motion_limit = 11000  # Number of moves to ensure ant has entered repeating cycle

if total_plays >= random_motion_limit:
    remainder = (total_plays - random_motion_limit) % cycle_size    # Determine how many moves beyond the
                                                                    # initial phase are required to make the
                                                                    # remaining cycle phase an even multiple of cycle_size
    phase_one_plays = random_motion_limit + remainder
    phase_two_plays = (total_plays - phase_one_plays) // cycle_size  # Determine how many cycles are in the cycle phase
else:
    phase_one_plays = total_plays
    phase_two_plays = 0

# Initialize rows x cols grid
# 0 = white, 1 = black
grid = [ [0 for x in range( cols )] for y in range( rows ) ]

# Initialize starting location to approximate grid center, facing 1 (of 4, e.g., North)
xpos = cols // 2
ypos = rows // 2
direction = 1

# Initialize counter of total black squares
total_blacks = 0

# Initialize counter of total plays. This allows confirmation that the total number of moves was the expected number
cur_play = 0

# Execute the random motion phase
for play in range(phase_one_plays):
    if xpos >= cols or xpos < 0 or ypos >= rows or ypos < 0:
        print ('Error: exceeded boundary of grid at (',xpos,',',ypos,')')
        break

    if grid[xpos][ypos] == 0:    # On white
        onWhite()
        total_blacks += 1   # We flipped the square to black
    else:
        onBlack()
        total_blacks -= 1   # We flipped the square to white

    cur_play += 1

# Run a single cycle to determine how many blacks are added in a cycle (spoiler: 12)
additional_blacks = 0
for moves in range (cycle_size):
    if xpos >= cols or xpos < 0 or ypos >= rows or ypos < 0:
        print ('Error: exceeded boundary of grid at (',xpos,',',ypos,')')
        break

    if grid[xpos][ypos] == 0:    # On white
        onWhite()
        additional_blacks += 1   # We flipped the square to black
    else:
        onBlack()
        additional_blacks -= 1   # We flipped the square to white

# Multiply the number of cycles by the number of blacks flipped per cycle to get the total number of new
# new blacks, and add those to the overall total
total_blacks += (additional_blacks * phase_two_plays)

# Add additional moves accounted for by the above logic
cur_play += phase_two_plays * cycle_size

# May I have the enevelope with the results, please?
print('Total plays:', cur_play)
print('Total blacks: ', total_blacks)
