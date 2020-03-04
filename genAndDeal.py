import random

def genCardPack():
    cardPack = []
    suits = ['H','S','C','D']
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
    for suit in suits:
        for card in cards:
            cardPack.append(card+suit)
    return cardPack

def shuffleCardPack(cardPack):
    for i in range(1000000):
        cardSelection = random.randint(0, 51)
        cardPack[0], cardPack[cardSelection] = cardPack[cardSelection], cardPack[0]
    return cardPack

def formPlayerHands(playerCount):
    playerHands = []
    for i in range(playerCount):
        playerHands.append(['',''])
    return playerHands

def dealP1(cardPack, playerCount):
    playerHands = formPlayerHands(playerCount)
    for player in range(playerCount):
        for i in range(2):
            playerHands[player][i] = cardPack.pop()
    return playerHands, cardPack

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
    
def genAndDeal(playerCount):

    cardPack = shuffleCardPack(genCardPack())
    playerHands, cardPack = dealP1(cardPack, playerCount)
    return playerHands, cardPack
