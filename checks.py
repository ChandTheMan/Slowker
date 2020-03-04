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
            
def highCardCheck(hand, suitToCheck = False): 
    if suitToCheck:
        for i in range(len(hand)-1, -1, -1):
            if hand[i][1] == suitToCheck:
                return hand[i]
    return hand[-1]

def pairCheck(hand): 
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

def tripsCheck(hand):
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

def straightCheck(hand): 
    straightList = [faceCardConvert(hand[0][0])]
    
    for i in range(1, len(hand)):
        if faceCardConvert(hand[i][0]) == straightList[-1]:
            continue
        elif faceCardConvert(hand[i][0]) != straightList[-1]+1 and len(straightList) < 5:
            straightList = [faceCardConvert(hand[i][0])]       
        elif faceCardConvert(hand[i][0]) == straightList[-1]+1 and len(straightList) == 5:
            straightList.pop(0)
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