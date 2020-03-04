"""Pack functions."""
import random


def gen_card_pack():
    card_pack = []
    suits = ['H', 'S', 'C', 'D']
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
    for suit in suits:
        for card in cards:
            card_pack.append(card+suit)
    return card_pack


def shuffle_card_pack(card_pack):
    for i in range(1000000):
        card_selection = random.randint(0, 51)
        card_pack[0], card_pack[card_selection] = card_pack[card_selection], card_pack[0]
    return card_pack


def form_player_hands(player_count):
    player_hands = []
    for i in range(player_count):
        player_hands.append(['',''])
    return player_hands


def deal_p1(card_pack, player_count):
    player_hands = form_player_hands(player_count)
    for player in range(player_count):
        for i in range(2):
            player_hands[player][i] = card_pack.pop()
    return player_hands, card_pack


def deal_flop(card_pack):
    board = []
    for i in range(3):
        card_pack.pop()
        board.append(card_pack.pop())
    return board, card_pack


def deal_turn(board, card_pack):
    card_pack.pop()
    board.append(card_pack.pop())
    return board, card_pack


def deal_river(board, card_pack):
    card_pack.pop()
    board.append(card_pack.pop())
    return board, card_pack

    
def gen_and_deal(player_count):
    card_pack = shuffle_card_pack(gen_card_pack())
    player_hands, card_pack = deal_p1(card_pack, player_count)
    return player_hands, card_pack
