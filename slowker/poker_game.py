from card_pack import card_pack
from bet_round import bet_round

class poker_game:
    def __init__(self, bb):
        self.bb_index = 0
        self.bb = bb
        self.player_list = []
        self.board = []
        return
    
    def add_player(self, player):
        self.player_list.append(player)
        return
    
    def form_player_hands(self):    #The meat of this class - gens, shuffles and deals the cards
        self.card_pack = card_pack()
        self.card_pack.gen_card_pack()
        self.card_pack.shuffle_card_pack()
        for i in range(len(self.player_list)):
            for j in range(2):
                self.player_list[i].hand.append(self.card_pack.pop())
        return
    
    def update_all_hands(self):     #Calculates hand of each player
        for i in range(len(self.player_list)):
            self.player_list[i].hand_calculate(self.board)
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

    def first_bet(self):
        a = bet_round(self)
        a.bet_first_round()
        return

    def standard_bet_round(self):
        a.standard_bet()
        return