from hand_calculate import hand_calculate

### Completely all over the place ###


def hand_compare(player_hands, board):  # INCOMPLETE
    """I'm not sure what's happening here."""
    hand_values = []
    for i in range(len(player_hands)):
        hand_values.append(hand_calculate(player_hands[i], board))
    hand_count = [0, 0, 0, 0, 0, 0, 0, 0]
    print(hand_values)
    for i in range(len(hand_values)):
        
        hand_count[hand_values[i][2]-1] += 1
    print(hand_count)
    return
    

# Hierachy of hands to compare
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

# Michaels Code -need to comb through this and intergrate possiby-
"""
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

"""