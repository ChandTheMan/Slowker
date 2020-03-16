# from slack import WebClient


from player import player
from poker_game import poker_game
from bet_round import bet_round

player_1 = player("Corey", 500) #Create player, with name, bankroll
player_2 = player("Algy", 420)
player_3 = player("Michael \'Mr. Finternational\' Finn", 100)
player_4 = player("Rex", 5000)


def main():
    """Slowker is slow poker!"""
    game = poker_game(20)
    game.add_player(player_1)   #Temp solution to add players to game
    game.add_player(player_2)
    game.add_player(player_3)
    game.add_player(player_4)
    game.form_player_hands()    #Deal phase one, creating card objects and card_pack  
    game.update_all_hands()     #Used after each round, to sort hand + calculate each persons strongest hand
    game.first_bet()
    game.deal_flop()
    game.update_all_hands()
    #game.standard_bet_round()
    game.deal_turn()
    game.update_all_hands()
    #game.standard_bet_round()
    game.deal_river()
    game.update_all_hands()
    #game.standard_bet_round()
    #print(game.player_list[1].hand_value)   #Prints hand_value of player at index 1
    #hand_compare.hand_compare(player_hands, board) --Incomplete
    return

main()
#if __name__ == "__main__":
    # Main function call to run
    #main(player_count=8)
