"""Pack functions."""
import random
from hand_calculate import hand_compute
class player:
    def __init__(self, name, bank_roll):
        self.name = name
        self.bank_roll = bank_roll
        self.hand = []
        self.hand_worth = []
        self.hand_value = []
        return

    def update_total_hand(self, board):
        self.total_hand = self.hand + board
        return

    def hand_sort_number(self):
        """Sort a hand by the numerical representation of each card A->K."""
        for i in range(len(self.total_hand)-1):
            current_min = self.total_hand[i].raw_value
            index = i
            for j in range(i+1, len(self.total_hand)):
                selection = self.total_hand[j].raw_value
                if selection < current_min:
                    current_min = selection
                    index = j
            self.total_hand[i], self.total_hand[index] = self.total_hand[index], self.total_hand[i]
        return

    def print_icon(self):
        for i in range(len(self.total_hand)):
            print(self.total_hand[i].icon, end=" ")
        return
    
    def hand_sort_suit(self):
        for i in range(len(self.total_hand), -1, -1):
            for j in range(0, i-1):
                if self.total_hand[j].suit > self.total_hand[j+1].suit:
                    self.total_hand[j], self.total_hand[j+1] = self.total_hand[j+1], self.total_hand[j]
        return

    def hand_calculate(self, board):
        """Find combinations present in a given hand when referencing the current board.."""
        self.update_total_hand(board)
        self.hand_sort_suit()
        self.hand_sort_number()
        self.hand_value = hand_compute(self.total_hand)
        return

class card:
    def __init__(self, value, suit):
        self.icon = value + suit
        self.value = value
        self.suit = suit
        try:
            self.raw_value = int(value)
        except ValueError:
            self.raw_value = self.face_card_convert()
        return

    def face_card_convert(self):
        """Convert from a deck card A->K into it's numerical representation."""
        if self.value == 'A':
            return 1
        elif self.value == 'X':
            return 10
        elif self.value == 'J':
            return 11
        elif self.value == 'Q':
            return 12
        elif self.value == 'K':
            return 13

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
        

class game:
    def __init__(self):
        self.player_list = []
        self.board = []
        return
    
    def add_player(self, player):
        self.player_list.append(player)
        return
    
    def form_player_hands(self):
        self.card_pack = card_pack()
        self.card_pack.gen_card_pack()
        self.card_pack.shuffle_card_pack()

        for i in range(len(self.player_list)):
            for j in range(2):
                self.player_list[i].hand.append(self.card_pack.pop())
        return
    
    def update_all_hands(self):
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
