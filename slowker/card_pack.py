from card import card
import random

class card_pack:
    def __init__(self):
        self.card_pack = []
        return

    def gen_card_pack(self):
        suits = ['H', 'S', 'C', 'D']
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
        for suit in suits:
            for value in cards:
                self.card_pack.append(card(value, suit))
        return    

    def shuffle_card_pack(self):
        for i in range(1000000):
            card_selection = random.randint(0, 51)
            self.card_pack[0], self.card_pack[card_selection] = self.card_pack[card_selection], self.card_pack[0]
        return
    
    def pop(self): #Super hacky
        return self.card_pack.pop()