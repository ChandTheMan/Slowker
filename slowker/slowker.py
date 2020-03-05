# from slack import WebClient

from gen_and_deal import game
from gen_and_deal import player

player_1 = player("Corey", 500)
player_2 = player("Algy", 420)

def main():
    """Slowker is slow poker!"""
    gamey = game()
    gamey.add_player(player_1) #Temp solution to add players
    gamey.add_player(player_2)
    gamey.gen_card_pack()
    gamey.shuffle_card_pack()
    gamey.form_player_hands()
    gamey.deal_flop()
    gamey.deal_turn()
    gamey.deal_river()
    print(gamey.player_list[0].hand)
    #hand_compare.hand_compare(player_hands, board)

    return

main()
#if __name__ == "__main__":
    # Main function call to run
    #main(player_count=8)
