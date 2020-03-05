import checks
###Re think name for this file ###

def hand_compute(hand):
    """Find combinations present in a given hand when referencing the current board.."""
    container = checks.flush_check(hand)
    if container:
        return container, 'flush', 5
    container = checks.straight_check(hand)
    if container:
        return container, 'straight', 4
    container = checks.trips_check(hand)
    if container:
        return container, 'trips', 3
    container = checks.pair_check(hand)
    if container:
        return container, 'pair', 2
    return checks.high_card_check(hand, 'highcard')     #This may be broken... is returning just one value... maybe...
