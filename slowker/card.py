class card:
    def __init__(self, value, suit):
        self.icon = value + suit    #The display of the card eg 'AH'
        self.value = value
        self.suit = suit
        try:
            self.raw_value = int(value)     #Stores the value of the card as an int (used for sorting later)
        except ValueError:
            self.raw_value = self.face_card_convert()
        return

    def face_card_convert(self):
        """Convert from a deck card A->K into it's numerical representation."""
        if self.value == 'A':
            return 1
        elif self.value == 'X':
            return 10
        elif self.value == 'J':
            return 11
        elif self.value == 'Q':
            return 12
        elif self.value == 'K':
            return 13