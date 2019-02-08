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
    suits = [card[1] for card in hand]
    suitset = set(suits)
    if len(suitset) == 1:
        return True
    else:
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
print (flush)
