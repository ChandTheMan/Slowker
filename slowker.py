#from slack import WebClient
from genAndDeal import genAndDeal
from genAndDeal import dealFlop
from genAndDeal import dealTurn
from genAndDeal import dealRiver
from handCalculate import handCalculate
from handCompare import handCompare
       
def main(playerCount):
    playerHands, cardPack = genAndDeal(playerCount)
    board, cardPack = dealFlop(cardPack)
    board, cardPack = dealTurn(board, cardPack)
    board, cardPack = dealRiver(board, cardPack)
    print(board)
    handCompare(playerHands, board)
    return
          
main(8) #Main function call to run