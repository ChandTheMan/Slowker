"""Deck/Hand based checks to perform."""


def face_card_convert(card):
    """Convert from a deck card A->K into it's numerical representation."""
    try:
        return int(card)
    except ValueError:
        if card == 'A':
            return 1
        elif card == 'X':
            return 10
        elif card == 'J':
            return 11
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13


def high_card_check(hand, suit_to_check: str):
    """Get the highest card in a given hand.

    Accepts suit parameter, allowing a high card of a specific suit to be found.
    """
    if suit_to_check:
        for i in range(len(hand)-1, -1, -1):
            if hand[i][1] == suit_to_check:
                return hand[i]
    return hand[-1]


def pair_check(hand):
    """Find pairs in a given hand."""

    pair_list = []
    for i in range(len(hand)-1):
        try:
            if hand[i][0] == hand[i+1][0] and hand[i+1][0] != pair_list[-1]:
                pair_list.append(hand[i][0])
        except IndexError:
            if hand[i][0] == hand[i+1][0]:
                pair_list.append(hand[i][0])
    if len(pair_list) == 0:
        return False
    if len(pair_list) <= 2:
        return pair_list
    return [pair_list[-2], pair_list[-1]]


def trips_check(hand):
    """Find triples in a given hand."""
    tripsList = []
    for i in range(len(hand)-2):
        try:
            if hand[i][0] == hand[i+1][0] == hand[i+2][0] and hand[i+1][0] != tripsList[-1]:
                tripsList.append(hand[i][0])
        except IndexError:
            if hand[i][0] == hand[i+1][0] == hand[i+2][0]:
                tripsList.append(hand[i][0])
    if len(tripsList) == 0:
        return False
    return tripsList[-1]


def straight_check(hand):
    """Find straights in a given hand."""
    straight_list = [face_card_convert(hand[0][0])]
    
    for i in range(1, len(hand)):
        if face_card_convert(hand[i][0]) == straight_list[-1]:
            continue
        elif face_card_convert(hand[i][0]) != straight_list[-1]+1 and len(straight_list) < 5:
            straight_list = [face_card_convert(hand[i][0])]
        elif face_card_convert(hand[i][0]) == straight_list[-1]+1 and len(straight_list) == 5:
            straight_list.pop(0)
            straight_list.append(face_card_convert(hand[i][0]))
        elif face_card_convert(hand[i][0]) == straight_list[-1]+1:
            straight_list.append(face_card_convert(hand[i][0]))
        elif face_card_convert(hand[i][0]) != straight_list[-1]+1 and len(straight_list) == 5:
            return straight_list

    if len(straight_list) < 5:
        return False
    else:
        return straight_list


def flush_check(hand):
    """Find flush in a given hand."""
    suit_count = [0, 0, 0, 0]
    for i in hand:
        if i[1] == 'C':
            suit_count[0] += 1
            if suit_count[0] == 5:
                return high_card_check(hand, 'C')
        elif i[1] == 'D':
            suit_count[1] += 1
            if suit_count[1] == 5:
                return high_card_check(hand, 'D')
        elif i[1] == 'H':
            suit_count[2] += 1
            if suit_count[2] == 5:
                return high_card_check(hand, 'H')
        elif i[1] == 'S':
            suit_count[3] += 1
            if suit_count[3] == 5:
                return high_card_check(hand, 'S')
    return False
