#-------------------------------------------------------------------
# Problem 349 - David Oxford - 2/9/2019
#-------------------------------------------------------------------

def move():
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
    grid[xpos][ypos] = 1    # Turn black
    turn('CW')
    move()

#-------------------------------------------------------------------
def onBlack():
    grid[xpos][ypos] = 0    # Turn white
    turn('CCW')
    move()

#-------------------------------------------------------------------
print('Initializing...')

# Set playing grid size
rows = 20000
cols = 20000

total_plays = 1000000

# Initialize rows x cols grid
# 0 = white, 1 = black
grid = [ [0 for x in range( cols )] for y in range( rows ) ]

# Initialize globals for starting location to approx
# center of grid, facing 1 (of 4, e.g., North)
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

    cur_play += 1
    if cur_play % tenths == 0:
        pct_done = (cur_play / total_plays) * 100
        print(int(pct_done), "%")



    #print('[',xpos, ',', ypos, ']')
    #for row in range(rows):
    #    disp_row = str(row) + '|'
    #    for col in range(cols):
    #        disp_row = disp_row +' ' + str(grid[row][col])
    #    print(disp_row)

    #print ('   -------------------')
    #print ('   0 1 2 3 4 5 6 7 8 9')
    #print ('-----')

#print(grid[3][5])
#print(grid[4][5])
#print(grid[4][6])
#print(grid[3][6])
#print(grid[2][5])
#print(grid[9][8])

total_blacks = 0
for row in range(rows):
    total_blacks += sum(grid[row])

print('Total blacks: ', total_blacks)
print('Ending position [', xpos, ',', ypos, ']')
print('Total plays:', cur_play)
print('X max and min:', maxx, minx)
print('Y max and min:', maxy, miny)
