class Card:
    # תצוגת קלף במשחק הקלפים
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit


    # כתיבת הקלף והמרה של משתנים לסוגים של קלפים שונים
    def __repr__(self):
        if self.value==1 or self.value > 10:
            return f"{numdict[self.value]} {suitdict[self.suit]}"
        return f"{self.value} {suitdict[self.suit]}"

numdict = {1:"A", 11:"J", 12:"Q", 13:"K"}
suitdict = {0:"♦",1:'♠',2:'♥',3:'♣'}
