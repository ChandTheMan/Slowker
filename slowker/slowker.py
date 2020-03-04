# from slack import WebClient

import gen_and_deal
import hand_compare


def main(player_count):
    """Slowker is slow poker!"""
    player_hands, card_pack = gen_and_deal.gen_and_deal(player_count)
    board, card_pack = gen_and_deal.deal_flop(card_pack)
    board, card_pack = gen_and_deal.deal_turn(board, card_pack)
    board, card_pack = gen_and_deal.deal_river(board, card_pack)
    print(board)
    hand_compare.hand_compare(player_hands, board)
    return


if __name__ == "__main__":
    # Main function call to run
    main(player_count=8)
