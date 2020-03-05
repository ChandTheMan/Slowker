"""Pack functions."""
import random
class player:
    def __init__(self, name, bank_roll):
        self.name = name
        self.bank_roll = bank_roll
        self.hand = []
        return

class game:
    def __init__(self):
        self.player_list = []
        self.board = []
        return
    
    def add_player(self, player):
        self.player_list.append(player)
        return
    
    def gen_card_pack(self):
        card_pack = []
        suits = ['H', 'S', 'C', 'D']
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
        for suit in suits:
            for card in cards:
                card_pack.append(card+suit)
        self.card_pack = card_pack
        return

    def shuffle_card_pack(self):
        for i in range(1000000):
            card_selection = random.randint(0, 51)
            self.card_pack[0], self.card_pack[card_selection] = self.card_pack[card_selection], self.card_pack[0]
        return

    def form_player_hands(self):
        for i in range(len(self.player_list)):
            for j in range(2):
                self.player_list[i].hand.append(self.card_pack.pop())
        return

    def deal_flop(self):
        for i in range(3):
            self.card_pack.pop()
            self.board.append(self.card_pack.pop())
        return

    def deal_turn(self):
        self.card_pack.pop()
        self.board.append(self.card_pack.pop())
        return

    def deal_river(self):
        self.card_pack.pop()
        self.board.append(self.card_pack.pop())
        return










'''
def gen_and_deal(player_count):
    card_pack = shuffle_card_pack(gen_card_pack())
    player_hands, card_pack = deal_p1(card_pack, player_count)
    return player_hands, card_pack
'''