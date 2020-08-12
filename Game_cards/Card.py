class Card:
    # תצוגת קלף במשחק הקלפים
    def __init__(self, value, suit):
        if type (value)== int:
            if 0<value<14:
                self.value = value
            elif value>13:
                self.value = 0
            elif value<1:
                self.value = 0
        if type (value)!= int:
            self.value=1

        if type (suit)==int:
            if 0<suit<4:
                self.suit=suit
            elif suit==0:
                self.suit=suit
            elif suit<0:
                self.suit=0
            elif suit>14:
                self.suit=0

        else:
            self.suit==0




    # כתיבת הקלף והמרה של משתנים לסוגים של קלפים שונים
    def __repr__(self):
        if self.value == 1 or self.value > 10:
            return f"{numdict[self.value]} {suitdict[self.suit]}"
        return f"{self.value} {suitdict[self.suit]}"


numdict = {1: "A", 11: "J", 12: "Q", 13: "K"}
suitdict = {0: "♦", 1: '♠', 2: '♥', 3: '♣'}
