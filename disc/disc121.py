#-------------------------------------------------------------------
# Problem 121 - David Oxford - 2/10/2019
#-------------------------------------------------------------------
# A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its
# colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.
#
# The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.
#
# If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum
# prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss.
# Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in
#  the example given the player actually wins £9.
#
# Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.

# 438   total wins out of 1000000 games played.
# 446   total wins out of 1000000 games played.
# 477   total wins out of 1000000 games played.
# 441   total wins out of 1000000 games played.
# 4386  total wins out of 10000000 games of 15 picks played.
# 4450  total wins out of 10000000 games of 15 picks played.
# 4441  total wins out of 10000000 games of 15 picks played.

#-------------------------------------------------------------------
def pickDisc(bag):
    pick = random.randrange(len(bag))
    return bag[pick]

#-------------------------------------------------------------------
def playGame(NUM_PICKS):
    # Define "constants"
    RED = 0
    BLUE = 1

    # Initialize
    bag = [RED, BLUE]
    total_blues = 0

    for play in range(NUM_PICKS):
        pick = pickDisc(bag)
        if pick == BLUE:
            total_blues += 1
            #print("Player picked blue")
        else:
            pass
            #print("Player picked red")

        bag.append(RED)

    if total_blues > NUM_PICKS/2:
        return(1)
        #print('Player wins!')
    else:
        return(0)
        #print('Player loses again!')

    #print (total_blues, 'total blue discs drawn in', NUM_PLAYS, 'plays.')

#-------------------------------------------------------------------
import random

NUM_PLAYS = 10000000
NUM_PICKS = 15

total_wins = 0

for play in range(NUM_PLAYS):
    total_wins += playGame(NUM_PICKS)

print(total_wins, ' total wins out of', NUM_PLAYS, 'games of', NUM_PICKS, 'picks played.')
