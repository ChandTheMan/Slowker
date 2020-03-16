
class bet_round():
    def __init__(self, poker_game):
        self.pot = 0
        self.player_list = poker_game.player_list
        self.bb_index = poker_game.bb_index
        self.bb = poker_game.bb
        for i in range(len(self.player_list)):
            self.player_list[i].play_status = True
            self.player_list[i].self_pot = 0       
            return

    def set_bet(self, play_container):
        if play_container[2] == 'bet':
            self.end_pointer = self.game_pointer
            #self.temp_pointer = False
            self.current_bet = play_container[3]
            return
        return

    def bet_loop(self):
        counter = 0
        while self.game_pointer != self.end_pointer or counter == 0:
            print("The current bet is: ", self.current_bet, end ='\n')
            print("You have contributed ", self.player_list[self.game_pointer].self_pot, " in this round of betting", end = '\n')
            print(self.current_bet-self.player_list[self.game_pointer].self_pot, "to call", end = '\n')
            if self.player_list[self.game_pointer].play_status:
                print("The action is on: ", self.player_list[self.game_pointer].name, end = '\n')
                play_container = []
                play_container = self.player_list[self.game_pointer].player_action_call(input("What do you want to do?: "), self.current_bet)
                self.pot += play_container[0]
                self.player_list[self.game_pointer].play_status = play_container[1]
                self.set_bet(play_container) 
                print('\n')
            self.game_pointer = find_correct_index(len(self.player_list), self.game_pointer)
            counter = 1
           
        print("--- BETTING OVER - POT IS: ", self.pot, " ---")
        return

    def bet_first_round(self):
        self.pot += self.player_list[self.bb_index].call(self.bb)[0]
        self.pot += self.player_list[self.bb_index-1].call(self.bb/2)[0]
        self.current_bet = self.bb
        self.end_pointer = find_correct_index(len(self.player_list), self.bb_index)
        self.game_pointer = find_correct_index(len(self.player_list), self.bb_index)
        #print("we are here")
        self.bet_loop()
        
        return

    def standard_bet(self):
        for i in range(len(self.player_list)):
            self.player_list[i].self_pot = 0       
        self.current_bet = 0
        self.end_pointer = find_correct_index(len(self.player_list), self.bb_index, 'backward')
        self.game_pointer = find_correct_index(len(self.player_list), self.bb_index, 'backward')
        self.bet_loop()
        return


def find_correct_index(player_count, index, direction='forward'):
    if direction == 'forward':
        if index == player_count-1:
            return 0
        else: 
            return index+1
    elif direction == 'backward':
        if index == 0:
            return player_count-1
        else: 
            return index-1
        

        
