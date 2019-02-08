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
    for x in range(1, len(ranks)):
        cur_rank = ranks[x]
        if cur_rank in rank_counts.keys():
            rank_counts[cur_rank] = rank_counts[cur_rank] + 1
        else:
            rank_counts[cur_rank] = 1

    return rank_counts

#-------------------------------------------------------------------
def isFourOfAKind(hand):
    pairings = checkPairings(hand)  #Get dict of rank / counts

    for rank in pairings:
        if pairings[rank] == 4:   #If that rank has four cards in the pairing dict
            return rank

    return False

#-------------------------------------------------------------------

f = open('poker.txt')
hands = f.readline()
f.close()

hand1 = hands[0:14]
hand1 = hand1.split(' ')

hand2 = hands[15:29]
hand2 = hand2.split(' ')

#print (hand1)
#print (hand2)

ha1=[]
ha2=[]

for card in hand1:
    p1 = cardval(card[0:1])
    p2 = card[1:2]
    ha1.append((p1,p2))

#for card in hand2:
#    p1 = cardval(card[0:1])
#    p2 = card[1:2]
#    ha2.append((p1,p2))

ha1.sort(reverse=True)
#ha2.sort(reverse=True)

print(ha1)
#print(ha2)

flush = isFlush(ha1)
print ('Flush?', flush)

straight = isStraight(ha1)
print ('Straigh?', straight)

straight = isStraightFlush(ha1)
print ('Straight Flush?', straight)

straight = isRoyalFlush(ha1)
print ('Royal Flush?', straight)

pairings = checkPairings(ha1)
print ('Pairings:', pairings)

foak = isFourOfAKind(ha1)
print ('Four of a Kind?', foak)
