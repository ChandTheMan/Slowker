from hand_calculate import hand_compute

class player:
    def __init__(self, name, bank_roll):
        self.name = name
        self.bank_roll = bank_roll
        self.play_status = True #True for in play, false for folded
        self.hand = []
        self.hand_worth = []    #Empty container for later hand worth rank
        self.hand_value = []    #Empty container for hand value storage from check function
        self.self_pot = 0
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
    
    def bet(self, bet_amount):
        assert bet_amount <= self.bank_roll, "Bet is higher than bank roll"
        self.bank_roll -= bet_amount-self.self_pot
        final_amount = bet_amount-self.self_pot
        self.self_pot = bet_amount
        return [final_amount, self.play_status, 'bet', bet_amount]
    
    def call(self, amount):
        if self.bank_roll < amount-self.self_pot:
            amount = self.bank_roll
            self.bank_roll = 0
            self.self_pot += amount
            return [amount, self.play_status, 'call']
        else:
           
            self.bank_roll -= amount-self.self_pot
            final_amount = amount-self.self_pot
            self.self_pot += amount-self.self_pot
        
            return [final_amount, self.play_status, 'call']
    
    def fold(self):
        self.play_status = False
        return [0, self.play_status, 'fold']

    def player_action_call(self, action, current_bet):
        while True:
            if action == 'bet':
                return self.bet(int(input("How much to bet?: ")))
            if action == 'call':
                return self.call(current_bet)
            if action == 'fold':
                return self.fold()
            if action == 'check cards':
                print("Your hand is: ", end = "") 
                print(self.hand[0].icon, self.hand[1].icon)
            action = input("What would you like to do now?: ")


    def print_icon(self):       #A method to print a players cards, don't use regular print!
        for i in range(len(self.total_hand)):
            print(self.total_hand[i].icon, end=" ")
        return

