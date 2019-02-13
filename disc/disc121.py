#-------------------------------------------------------------------
# David Oxford - 2/10/2019
# https://github.com/davidoxford/euler/tree/master/disc
#
#-------------------------------------------------------------------
# Project Euler Problem 121
# https://projecteuler.net/problem=121
#
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
#-------------------------------------------------------------------
#
# Initial approach is to do a Monte Carlo simulation. This is a slow, estimation-based approach and non-optimal
#
#-------------------------------------------------------------------
def pickDisc(bag):
    pick = random.randrange(len(bag))
    return bag[pick]

#-------------------------------------------------------------------
def playGame(num_picks):
    # Define "constants"
    RED = 0
    BLUE = 1

    # Initialize
    bag = [RED, BLUE]
    total_blues = 0

    for play in range(num_picks):
        pick = pickDisc(bag)
        if pick == BLUE:
            total_blues += 1

        bag.append(RED)

    if total_blues > num_picks/2:
        return(1)
    else:
        return(0)

#-------------------------------------------------------------------
import random

NUM_PLAYS = 10000000
NUM_PICKS = 15

total_wins = 0

for play in range(NUM_PLAYS):
    total_wins += playGame(NUM_PICKS)

print(total_wins, ' total wins out of', NUM_PLAYS, 'games of', NUM_PICKS, 'picks played.')
