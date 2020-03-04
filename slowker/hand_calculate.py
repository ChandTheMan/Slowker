import checks


def hand_sort_number(hand):
    """Sort a hand by the numerical representation of each card A->K."""
    for i in range(len(hand)-1):
        current_min = checks.face_card_convert(hand[i][0])
        index = i
        for j in range(i+1, len(hand)):
            selection = checks.face_card_convert(hand[j][0])
            if selection < current_min:
                current_min = selection
                index = j
        hand[i], hand[index] = hand[index], hand[i]
    return hand


def hand_sort_suit(hand):
    """ Sort a hand by the suits present.

    suitCount = [0, 0, 0, 0]
    for i in hand:
        if i[1] == 'C':
            suitCount[0] += 1
        elif i[1] == 'D':
            suitCount[1] += 1
        elif i[1] == 'H':
            suitCount[2] += 1
        elif i[1] == 'S':
            suitCount[3] += 1
    """
    for i in range(len(hand), -1, -1):
        for j in range(0, i-1):
            if hand[j][1] > hand[j+1][1]:
                hand[j], hand[j+1] = hand[j+1], hand[j]
    return hand 


def hand_calculate(hand, board):
    """Find combinations present in a given hand when referencing the current board.."""
    total_sorted_hand = hand_sort_number(hand_sort_suit(hand + board))
    container = checks.flush_check(total_sorted_hand)
    if container:
        return container, 'flush', 5
    container = checks.straight_check(total_sorted_hand)
    if container:
        return container, 'straight', 4
    container = checks.trips_check(total_sorted_hand)
    if container:
        return container, 'trips', 3
    container = checks.pair_check(total_sorted_hand)
    if container:
        return container, 'pair', 2
    return checks.high_card_check(total_sorted_hand, 'highcard')
