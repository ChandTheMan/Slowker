def high_card_check(hand, suit_to_check: str):
    """Get the highest card in a given hand.

    Accepts suit parameter, allowing a high card of a specific suit to be found.
    """
    if suit_to_check:
        for i in range(len(hand)-1, -1, -1):
            if hand[i].suit == suit_to_check:
                return hand[i].icon
    return hand[-1].icon


def pair_check(hand):
    """Find pairs in a given hand."""

    pair_list = []
    for i in range(len(hand)-1):
        try:
            if hand[i].value == hand[i+1].value and hand[i+1].value != pair_list[-1]:
                pair_list.append(hand[i].value)
        except IndexError:
            if hand[i].value == hand[i+1].value:
                pair_list.append(hand[i].value)
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
            if hand[i].value == hand[i+1].value == hand[i+2].value and hand[i+1].value != tripsList[-1]:
                tripsList.append(hand[i].value)
        except IndexError:
            if hand[i].value == hand[i+1].value == hand[i+2].value:
                tripsList.append(hand[i].value)
    if len(tripsList) == 0:
        return False
    return tripsList[-1]


def straight_check(hand):
    """Find straights in a given hand."""
    straight_list = [hand[0].raw_value]
    
    for i in range(1, len(hand)):

        if hand[i].raw_value == straight_list[-1]:
            continue
        elif hand[i].raw_value != straight_list[-1]+1 and len(straight_list) < 5:
            straight_list = [hand[i].raw_value]
        elif hand[i].raw_value == straight_list[-1]+1 and len(straight_list) == 5:
            straight_list.pop(0)
            straight_list.append(hand[i].raw_value)
        elif hand[i].raw_value == straight_list[-1]+1:
            straight_list.append(hand[i].raw_value)
        elif hand[i].raw_value != straight_list[-1]+1 and len(straight_list) == 5:
            return straight_list

    if len(straight_list) < 5:
        return False
    else:
        return straight_list


def flush_check(hand):
    """Find flush in a given hand."""
    suit_count = [0, 0, 0, 0]
    for i in hand:
        if i.suit == 'C':
            suit_count[0] += 1
            if suit_count[0] == 5:
                return high_card_check(hand, 'C')
        elif i.suit == 'D':
            suit_count[1] += 1
            if suit_count[1] == 5:
                return high_card_check(hand, 'D')
        elif i.suit == 'H':
            suit_count[2] += 1
            if suit_count[2] == 5:
                return high_card_check(hand, 'H')
        elif i.suit == 'S':
            suit_count[3] += 1
            if suit_count[3] == 5:
                return high_card_check(hand, 'S')
    return False
