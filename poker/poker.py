#-------------------------------------------------------------------
# Problem 54 - David Oxford - 2/8/2019
#-------------------------------------------------------------------

def cardval(cardnum):
    if cardnum == 'T':
        pval = 10
    elif cardnum == "J":
        pval = 11
    elif cardnum == "Q":
        pval = 12
    elif cardnum == "K":
        pval = 13
    elif cardnum == "A":
        pval = 14
    else:
        pval = int(cardnum)
    return pval
#-------------------------------------------------------------------
def isFlush(hand):
    first_card = hand[0]        #Look at the first card
    first_card_rank = first_card[0]

    suits = [card[1] for card in hand]
    suitset = set(suits)    #sets remove duplicates
    if len(suitset) == 1:
        return first_card_rank
    else:
        return False

#-------------------------------------------------------------------
def isStraight(hand):
    first_card = hand[0]        #Look at the first card
    first_card_rank = first_card[0]

    ranks = [card[0] for card in hand]  #Hand is assumed to be sorted in desc order

    for x in range(len(ranks)-1):    #Loop through the first four cards, looking at it and the next card
        if ranks[x+1] != ranks[x]-1: #If the next card isn't one less than this card, it ain't a straight
            return False

    return first_card_rank

#-------------------------------------------------------------------
def isStraightFlush(hand):
    first_card = hand[0]        #Look at the first card
    first_card_rank = first_card[0]

    if isStraight(hand) and isFlush(hand):
        return first_card_rank
    else:
        return False

#-------------------------------------------------------------------
def isRoyalFlush(hand):
    first_card = hand[0]        #Look at the first card
    if first_card[0] != 14:     #If the rank of the first card isn't 14 (Ace), it's not a royal flush
        return False

    if isStraight(hand) and isFlush(hand) :
        return 14
    else:
        return False

#-------------------------------------------------------------------
def checkPairings(hand):
    ranks = [card[0] for card in hand]  #Get list of ranks of current hand

    rank_counts = {ranks[0] : 1}  #Count the first card
    for x in range(1, len(ranks)):  #Loop through the remaining card ranks
        cur_rank = ranks[x]
        if cur_rank in rank_counts.keys():
            rank_counts[cur_rank] = rank_counts[cur_rank] + 1  #Increment the count for the current card rank
        else:
            rank_counts[cur_rank] = 1   #Append a new entry with the current card's rank

    return rank_counts

#-------------------------------------------------------------------
def isFourOfAKind(hand):
    pairings = checkPairings(hand)  #Get dict of rank / counts

    for rank in pairings:
        if pairings[rank] == 4:   #If that rank has four cards in the pairing dict
            return rank

    return False

#-------------------------------------------------------------------
def isFullHouse(hand):
    pairings = checkPairings(hand)  #Get dict of rank / counts

    if len(pairings) == 2:  #Full house will have two pairings, one with three cards, and one with two cards
        for rank in pairings:
            if pairings[rank] == 3:   #If that rank has three cards in the pairing dict
                three_card_rank = rank
            else:                     #Rank having two cards in the pairing dict
                two_card_rank = rank
        return three_card_rank + (two_card_rank/100) #Return a value with the two-card grouping as a decimal that
                                                     #allows easy comparison when the three-card grouping is the same in both hands
                                                     #e.g., 8's over 5's is returned as 8.05, which would beat 8's over 2's (8.05 > 8.02)
    else:
        return False

#-------------------------------------------------------------------
def isThreeOfAKind(hand):
    pairings = checkPairings(hand)  #Get dict of rank / counts

    if len(pairings) == 3:  #Three of a kind will have one rank with three values, and two more with one each, for a total of three ranks in the list
        for rank in pairings:
            if pairings[rank] == 3:   #If that rank has three cards in the pairing dict
                return rank

    return False

#-------------------------------------------------------------------
def isTwoPair(hand):
    pairings = checkPairings(hand)  #Get dict of rank / counts

    if len(pairings) == 3 and not isThreeOfAKind(hand):  #Two pair will have three pairings, two with two cards each, and one with one card
        ranks = list(pairings.keys())
        my_pairs = []
        for rank in ranks:
            if pairings[rank] == 2:
                my_pairs.append(rank)

        return my_pairs[0] + my_pairs[1]/100
    else:
        return False

#-------------------------------------------------------------------
def isOnePair(hand):
    pairings = checkPairings(hand)  #Get dict of rank / counts

    if len(pairings) == 4:  #One pair will have one rank with two values, and three more with one each, for a total of four ranks in the list
        for rank in pairings:
            if pairings[rank] == 2:   #If that rank has two cards in the pairing dict
                return rank

    return False

#-------------------------------------------------------------------
def getHandRankAndValue(hand):
    # Return a list of the form [Hand Rank, Hand Value]
    # Hand rank return values
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
    player1_resuluts = getHandRankAndValue(hands[0])
    player2_results = getHandRankAndValue(hands[1])

    if player1_resuluts[0] > player2_results[0]:
        return 0
    elif player2_results[0] > player1_resuluts[0]:
        return 1
    elif player1_resuluts[1] > player2_results[1]:
        return 0
    elif player2_results[1] > player1_resuluts[1]:
        return 1
    else:
        return 999

#-------------------------------------------------------------------

score=[0,0]

f = open('p054_poker.txt')
for game in f:

    #Tokenize raw game data

    raw_hand=[]
    # Parse player 1's hand
    raw_hand.append(game[0:14])
    raw_hand[0] = raw_hand[0].split(' ')
    #Parse player 2's hand
    raw_hand.append(game[15:29])
    raw_hand[1] = raw_hand[1].split(' ')

    hands=[ [] for x in range(len(raw_hand))]  #Initialize the hands list to the total number of players


    for player in range(len(raw_hand)):
        for card in raw_hand[player]:
            p1 = cardval(card[0:1])
            p2 = card[1:2]
            hands[player].append((p1,p2))

    #print(hands)

    hands[0].sort(reverse=True)
    hands[1].sort(reverse=True)

    #print(hands)
    #print(hands[0])
    #print(hands[1])

    winner = whoWon(hands)
    if winner != 999:
        score[winner] = score[winner] + 1
    else:
        print(hands[0], "-->", getHandRankAndValue(hands[0]))
        print(hands[1], "-->", getHandRankAndValue(hands[1]))
        print('-----')
        print('')

print (score)

f.close()
