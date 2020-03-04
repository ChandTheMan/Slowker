
import time
from slack import WebClient

#Just poker here on out
        


def dealFlop(cardPack):
    board = []
    for i in range(3):
        cardPack.pop()
        board.append(cardPack.pop())
    return board, cardPack

def dealTurn(board, cardPack):
    cardPack.pop()
    board.append(cardPack.pop())
    return board, cardPack

def dealRiver(board, cardPack):
    cardPack.pop()
    board.append(cardPack.pop())
    return board, cardPack

def faceCardConvert(card):
    try:
        return int(card)
    except ValueError:
        if card == 'A':
            return 1
        elif card == 'X':
            return 10
        elif card == 'J':
            return 11
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13

def handSortNumber(hand):
    for i in range(len(hand)-1):
        currentMin = faceCardConvert(hand[i][0])
        index = i
        for j in range(i+1, len(hand)):
            selection = faceCardConvert(hand[j][0])
            if selection < currentMin:
                currentMin = selection
                index = j
        hand[i], hand[index] = hand[index], hand[i]
    return hand

def handSortSuit(hand):
    '''
    suitCount = [0, 0, 0, 0]
    for i in hand:
        if i[1] == 'C':
            suitCount[0] += 1
        elif i[1] == 'D':
            suitCount[1] += 1
        elif i[1] == 'H':
            suitCount[2] += 1
        elif i[1] == 'S':
            suitCount[3] += 1
    '''
    for i in range(len(hand), -1, -1):
        for j in range(0, i-1):
            if hand[j][1] > hand[j+1][1]:
                hand[j], hand[j+1] = hand[j+1], hand[j]
    return hand 
            
def highCardCheck(hand, suitToCheck = False):    #sorted hand required
    if suitToCheck:
        for i in range(len(hand)-1, -1, -1):
            if hand[i][1] == suitToCheck:
                return hand[i]
    return hand[-1]

def pairCheck(hand):    #sorted hand required
    pairList = []
    for i in range(len(hand)-1):
        try:
            if hand[i][0] == hand[i+1][0] and hand[i+1][0] != pairList[-1]:
                pairList.append(hand[i][0])
        except IndexError:
            if hand[i][0] == hand[i+1][0]:
                pairList.append(hand[i][0])
    if len(pairList) == 0:
        return False
    if len(pairList) <= 2:
        return pairList
    return [pairList[-2], pairList[-1]]

def tripsCheck(hand):   #sorted hand needed
    tripsList = []
    for i in range(len(hand)-2):
        try:
            if hand[i][0] == hand[i+1][0] == hand[i+2][0] and hand[i+1][0] != tripsList[-1]:
                tripsList.append(hand[i][0])
        except IndexError:
            if hand[i][0] == hand[i+1][0] == hand[i+2][0]:
                tripsList.append(hand[i][0])
    if len(tripsList) == 0:
        return False
    return tripsList[-1]

def straightCheck(hand):    #sorted hand needed
    straightList = [faceCardConvert(hand[0][0])]
    
    for i in range(1, len(hand)):
        if faceCardConvert(hand[i][0]) == straightList[-1]:
            continue
        elif faceCardConvert(hand[i][0]) != straightList[-1]+1 and len(straightList) < 5:
            straightList = [faceCardConvert(hand[i][0])]       
        elif faceCardConvert(hand[i][0]) == straightList[-1]+1 and len(straightList) == 5:
            straightList.pop(0)
            #print(straightList)
            straightList.append(faceCardConvert(hand[i][0]))
        elif faceCardConvert(hand[i][0]) == straightList[-1]+1:
            straightList.append(faceCardConvert(hand[i][0]))
        elif faceCardConvert(hand[i][0]) != straightList[-1]+1 and len(straightList) == 5:
            return(straightList)

    if len(straightList) < 5:
        return False
    else:
        return straightList

def flushCheck(hand):
    suitCount = [0, 0, 0, 0]
    for i in hand:
        if i[1] == 'C':
            suitCount[0] += 1
            if suitCount[0] == 5:
                return highCardCheck(hand, 'C')
        elif i[1] == 'D':
            suitCount[1] += 1
            if suitCount[1] == 5:
                return highCardCheck(hand, 'D')
        elif i[1] == 'H':
            suitCount[2] += 1
            if suitCount[2] == 5:
                return highCardCheck(hand, 'H')
        elif i[1] == 'S':
            suitCount[3] += 1
            if suitCount[3] == 5:
                return highCardCheck(hand, 'S')
    return False
    

def handCalculate(hand, board):
    totalSortedHand = handSortNumber(handSortSuit(hand+board))
    container = flushCheck(totalSortedHand)
    if container:
        return container, 'flush', 5
    container = straightCheck(totalSortedHand)
    if container:
        return container, 'straight', 4
    container = tripsCheck(totalSortedHand)
    if container:
        return container, 'trips', 3
    container = pairCheck(totalSortedHand)
    if container:
        return container, 'pair', 2
    return highCardCheck(totalSortedHand), 'highcard', 1

def handCompare(playerHands, board): #INCOMPLETE
    handValues = []
    for i in range(len(playerHands)):
        handValues.append(handCalculate(playerHands[i], board))
    handCount = [0,0,0,0,0,0,0,0]
    print(handValues)
    for i in range(len(handValues)):
        
        handCount[handValues[i][2]-1] += 1
    print(handCount)
    return
    
    '''
    highCardCheck
    pair(s)Check
    tripsCheck
    straightCheck
    flushCheck
    fullHouseCheck
    fourOfAKindCheck
    straightFlushCheck
    
    '''

def main(playerCount):
    cardPack = shuffleCardPack(genCardPack())
    playerHands, cardPack = dealP1(cardPack, playerCount)
    board, cardPack = dealFlop(cardPack)
    board, cardPack = dealTurn(board, cardPack)
    board, cardPack = dealRiver(board, cardPack)
    print(board)
    handCompare(playerHands, board)
    #print(board, len(cardPack))
    
    return
'''
def main(playerCount):
    cardPack = shuffleCardPack(genCardPack())
    playerHands, cardPack = dealP1(cardPack, playerCount)
    board, cardPack = dealFlop(cardPack)
    board, cardPack = dealTurn(board, cardPack)
    board, cardPack = dealRiver(board, cardPack)
    return handCalculate(playerHands[0], board)
    #print(board, len(cardPack))
'''   
          
tick = time.perf_counter()
#print(tick)
main(8)
tock = time.perf_counter()
#print(tock-tick)
'''
cardHierarchy = ["2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K", "A"]
handHierarchy = ["highcard", "pair", "twopair", "trips", "straight", "flush", "fullhouse", "straightflush", "royalflush"]
def rankPlayerHands(hands):
    # Function to return an orderable string based on the hand and highest card
    def getHandValue(hand, highestCard):
        handIndex = str(handHierarchy.index(hand)) if handHierarchy.index(hand) >= 10 else "0" + str(handHierarchy.index(hand))
        cardIndex = str(cardHierarchy.index(highestCard)) if cardHierarchy.index(highestCard) >= 10 else "0" + str(cardHierarchy.index(highestCard))
        return handIndex + cardIndex
    # Order hands from best to worst
    orderedHands = reversed(sorted(hands, key=lambda hand: getHandValue(hand["hand"], hand["highestCard"])))
    # Check for ties
    ranked = []
    for hand in orderedHands:
        if not ranked:
            ranked.append([hand])
        else:
            thisRank = ranked[-1]
            if hand["hand"] == thisRank[0]["hand"] and hand["highestCard"] == thisRank[0]["highestCard"]:
                thisRank.append(hand)
                ranked[-1] = thisRank
            else:
                ranked.append([hand])
    # Print
    for i, rank in enumerate(ranked):
        rankStr = "Rank {}: ".format(str(i+1))
        for hand in rank:
            rankStr += "[{}] ".format(hand["player"])
        print(rankStr)
exampleHands = [
    {
        "player": "Michael",
        "hand": "flush",
        "highestCard": "A"
    },
    {
        "player": "Corey",
        "hand": "flush",
        "highestCard": "J"
    },
    {
        "player": "BV",
        "hand": "pair",
        "highestCard": "4"
    },
    {
        "player": "Mark",
        "hand": "straight",
        "highestCard": "5"
    },
    {
        "player": "Thomas",
        "hand": "straight",
        "highestCard": "6"
    },
        {
        "player": "Tim",
        "hand": "pair",
        "highestCard": "4"
    }
]
rankPlayerHands(exampleHands)

'''