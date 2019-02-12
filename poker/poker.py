#-------------------------------------------------------------------
# Problem 54 - David Oxford - 2/8/2019
#-------------------------------------------------------------------

def cardVal(card_num):
    if card_num ==   'T':
        return 10
    elif card_num == 'J':
        return 11
    elif card_num == 'Q':
        return 12
    elif card_num == 'K':
        return 13
    elif card_num == 'A':
        return 14
    else:
        return int(card_num)

#-------------------------------------------------------------------
def isFlush(hand):
    first_card = hand[0]
    first_card_rank = first_card[0] # Get value of the first (highest) card

    suits = [card[1] for card in hand]
    suitset = set(suits)    # Sets remove duplicates
    if len(suitset) == 1:
        return first_card_rank
    else:
        return False

#-------------------------------------------------------------------
def isStraight(hand):
    first_card = hand[0]
    first_card_rank = first_card[0] # Get value of the first (highest) card

    ranks = [card[0] for card in hand]  # Hand is assumed to be sorted in desc order

    for x in range(len(ranks)-1):    # Loop through the first four cards, looking at it and the next card
        if ranks[x+1] != ranks[x]-1: # If the next card isn't one less than this card, it ain't a straight
            return False

    return first_card_rank

#-------------------------------------------------------------------
def isStraightFlush(hand):
    first_card = hand[0]        # Look at the first card
    first_card_rank = first_card[0]

    if isStraight(hand) and isFlush(hand):
        return first_card_rank
    else:
        return False

#-------------------------------------------------------------------
def isRoyalFlush(hand):
    first_card = hand[0]        # Look at the first card
    if first_card[0] != 14:     # If the rank of the first card isn't 14 (Ace), it's not a royal flush
        return False

    if isStraight(hand) and isFlush(hand) :
        return 14
    else:
        return False

#-------------------------------------------------------------------
def checkPairings(hand):
    ranks = [card[0] for card in hand]  # Get list of ranks of current hand

    rank_counts = {ranks[0] : 1}  # Count the first card
    for x in range(1, len(ranks)):  # Loop through the remaining card ranks
        cur_rank = ranks[x]
        if cur_rank in rank_counts.keys():
            rank_counts[cur_rank] = rank_counts[cur_rank] + 1  # Increment the count for the current card rank
        else:
            rank_counts[cur_rank] = 1   # Append a new entry with the current card's rank

    return rank_counts

#-------------------------------------------------------------------
def isFourOfAKind(hand):
    pairings = checkPairings(hand)  # Get dict of rank / counts

    for rank in pairings:
        if pairings[rank] == 4:   # If that rank has four cards in the pairing dict
            return rank

    return False

#-------------------------------------------------------------------
def isFullHouse(hand):
    pairings = checkPairings(hand)  # Get dict of rank / counts

    if len(pairings) == 2:  # Full house will have two pairings, one with three cards, and one with two cards
        for rank in pairings:
            if pairings[rank] == 3:   # If that rank has three cards in the pairing dict
                three_card_rank = rank
            else:                     # Rank having two cards in the pairing dict
                two_card_rank = rank
        return three_card_rank + (two_card_rank/100) # Return a value with the two-card grouping as a decimal that
                                                     # allows easy comparison when the three-card grouping is the same in both hands
                                                     # e.g., 8's over 5's is returned as 8.05, which would beat 8's over 2's (8.05 > 8.02)
    else:
        return False

#-------------------------------------------------------------------
def isThreeOfAKind(hand):
    pairings = checkPairings(hand)  # Get dict of rank / counts

    if len(pairings) == 3:  # Three of a kind will have one rank with three values, and two more with one each, for a total of three ranks in the list
        for rank in pairings:
            if pairings[rank] == 3:   # If that rank has three cards in the pairing dict
                return rank

    return False

#-------------------------------------------------------------------
def isTwoPair(hand):
    pairings = checkPairings(hand)  # Get dict of rank / counts

    if len(pairings) == 3 and not isThreeOfAKind(hand):  # Two pair will have three pairings, two with two cards each, and one with one card
        ranks = list(pairings.keys())
        my_pairs = []
        for rank in ranks:
            if pairings[rank] == 2:
                my_pairs.append(rank)

        return my_pairs[0] + my_pairs[1]/100    # Return a value with the lower-valued pair as a decimal that
                                                # allows easy comparison when the higher-value pair is the same in both hands
                                                # e.g., 8's and 5's is returned as 8.05, which would beat 8's and 2's (8.05 > 8.02)
    else:
        return False

#-------------------------------------------------------------------
def isOnePair(hand):
    pairings = checkPairings(hand)  # Get dict of rank / counts

    if len(pairings) == 4:  # One pair will have one rank with two values, and three more with one each, for a total of four ranks in the list
        for rank in pairings:
            if pairings[rank] == 2:   # If that rank has two cards in the pairing dict
                return rank

    return False

#-------------------------------------------------------------------
def highestCard(hands):
    # Assumes that there is a clear winner. Ties will return an arbitrary winner.

    # Build list of ranks for each hand
    ranks = []
    for x in range(len(hands)):
        ranklist = [card[0] for card in hands[x]]
        ranks.append(ranklist)

    best_card = max(hand for hand in ranks)
    best_hand = ranks.index(best_card)

    return best_hand

#-------------------------------------------------------------------
def getHandRankAndValue(hand):
    # Return a list of the form [Hand Rank, Hand Value]
    # Hand ranks:
    # 1 : High Card
    # 2 : One Pair
    # 3 : Two Pairs
    # 4 : Three of a Kind
    # 5 : Straight
    # 6 : Flush
    # 7 : Full House
    # 8 : Four of a Kind
    # 9 : Straight Flush
    # 10: Royal Flush

    if isRoyalFlush(hand):
        return [10, isRoyalFlush(hand)]

    if isStraightFlush(hand):
        return [9, isStraight(hand)]

    if isFourOfAKind(hand):
        return [8, isFourOfAKind(hand)]

    if isFullHouse(hand):
        return [7, isFullHouse(hand)]

    if isFlush(hand):
        return [6, isFlush(hand)]

    if isStraight(hand):
        return [5, isStraight(hand)]

    if isThreeOfAKind(hand):
        return [4, isThreeOfAKind(hand)]

    if isTwoPair(hand):
        return [3, isTwoPair(hand)]

    if isOnePair(hand):
        return [2, isOnePair(hand)]

    # Must be just a high card, so return the first value of the first element of hand (ie, the highest card, as they are sorted desc)
    return [1, hand[0][0]]

#-------------------------------------------------------------------
def whoWon(hands):
    global NUM_PLAYERS

    # Build a list of lists of the form [ [rank,value] [rank,value] ] for all hands
    player_results = [ getHandRankAndValue(hands[player]) for player in range(NUM_PLAYERS) ]

    # Determine the highest rank of any hands
    highest_rank = max(player[0] for player in player_results)

    # Build list of hands having the top rank (of the form [player#, hand rank, hand value])
    top_ranked_hands = []
    for player in range(len(player_results)):
        if player_results[player][0] == highest_rank:
            top_ranked_hands.append([player,player_results[player][0],player_results[player][1]])

    if len(top_ranked_hands) == 1:  # Unique winner
        return top_ranked_hands[0][0]   # Return the player number of the top-ranked hand
    else:
        # Determine the highest value of top-ranked hands
        highest_value = max(player[2] for player in top_ranked_hands)

        # Build list of top-ranked hands having the top value (of the form [player#, hand value])
        top_valued_hands = []
        for player in range(len(top_ranked_hands)):
            if top_ranked_hands[player][2] == highest_value:
                top_valued_hands.append([player,top_ranked_hands[player][2]])

        if len(top_valued_hands) == 1: # Unique winner
            return top_valued_hands[0][0]   # Return the player number of the top-valued hand
        else:    # Two or more hands have the same rank and same value
            # Build list of hands of possible winners
            possible_winning_hands = []
            for player in top_valued_hands:
                possible_winning_hands.append(hands[player[0]]) # Get the hand corresponding to the player #

            return highestCard(possible_winning_hands)

#-------------------------------------------------------------------
def main(game_file):
    global NUM_PLAYERS

    # Initialize score (count of games won) to 0 for all players
    score = [ 0 for x in range(NUM_PLAYERS)]

    f = open(game_file)
    for game in f:

        raw_hand=[]

        #Tokenize raw game data
        start_pos = 0
        end_pos = 14
        for player in range(NUM_PLAYERS):
            raw_hand.append(game[start_pos:end_pos])
            raw_hand[player] = raw_hand[player].split(' ')
            start_pos += 15
            end_pos += 15

        hands=[ [] for x in range(len(raw_hand))]  #Initialize the hands list to the total number of players

        # Build hands as list of tuples of the form: [[(7, 'C'), (6, 'D'), (5, 'H'), (5, 'D'), (3, 'S')]
        for player in range(len(raw_hand)):
            for card in raw_hand[player]:
                c1 = cardVal(card[0:1])         # First character is the rank (value) of the card. Assign number 2-14 (Ace = 14)
                c2 = card[1:2]                  # Second character is the suit
                hands[player].append((c1,c2))   # Add this card to 'player' hand

        # Sort hands into desc order based on rank
        for hand_num in range(len(hands)):
            hands[hand_num].sort(reverse=True)

        winner = whoWon(hands)
        score[winner] = score[winner] + 1   # Increment score of winning player

    f.close()

    # Report results
    for player in range(NUM_PLAYERS):
        print('Player', player+1, 'won', score[player], 'hands.')

#-------------------------------------------------------------------

# Define the total number of players per game in the input file
# All games must have the same number of players
NUM_PLAYERS = 2

# Execute main with name of the file to process
main('p054_poker.txt')
