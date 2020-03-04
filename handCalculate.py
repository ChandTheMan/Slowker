from checks import highCardCheck
from checks import pairCheck
from checks import tripsCheck
from checks import straightCheck
from checks import flushCheck
from checks import faceCardConvert
    
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