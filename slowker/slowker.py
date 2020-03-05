# from slack import WebClient


from player import player
from poker_game import poker_game

player_1 = player("Corey", 500) #Create player, with name, bankroll
player_2 = player("Algy", 420)


def main():
    """Slowker is slow poker!"""
    game = poker_game()
    game.add_player(player_1)   #Temp solution to add players to game
    game.add_player(player_2)
    game.form_player_hands()    #Deal phase one, creating card objects and card_pack  
    game.update_all_hands()     #Used after each round, to sort hand + calculate each persons strongest hand
    game.deal_flop()
    game.update_all_hands()
    game.deal_turn()
    game.update_all_hands()
    game.deal_river()
    game.update_all_hands()
    print(game.player_list[1].hand_value)   #Prints hand_value of player at index 1
    #hand_compare.hand_compare(player_hands, board) --Incomplete
    return

main()
#if __name__ == "__main__":
    # Main function call to run
    #main(player_count=8)
