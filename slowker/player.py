from hand_calculate import hand_compute

class player:
    def __init__(self, name, bank_roll):
        self.name = name
        self.bank_roll = bank_roll
        self.hand = []
        self.hand_worth = []    #Empty container for later hand worth rank
        self.hand_value = []    #Empty container for hand value storage from check function
        return

    def update_total_hand(self, board):     #Combines board and hand and keeps it in player data
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
    
    def hand_sort_suit(self):
        for i in range(len(self.total_hand), -1, -1):
            for j in range(0, i-1):
                if self.total_hand[j].suit > self.total_hand[j+1].suit:
                    self.total_hand[j], self.total_hand[j+1] = self.total_hand[j+1], self.total_hand[j]
        return

    def hand_calculate(self, board):    #Calls the hand_compute function, after sorting the hand
        """Find combinations present in a given hand when referencing the current board.."""
        self.update_total_hand(board)
        self.hand_sort_suit()
        self.hand_sort_number()
        self.hand_value = hand_compute(self.total_hand)
        return

    def print_icon(self):       #A method to print a players cards, don't use regular print!
        for i in range(len(self.total_hand)):
            print(self.total_hand[i].icon, end=" ")
        return

