from Game_cards.Card import Card
from random import shuffle


class Deckofcards:

    # איניט של חפיסת קלפים שלמה עפ הסוגים
    def __init__(self):
        self.deck = self._create()

    # יצירת חבילה למשחק
    def _create(self):
        deck = []
        for i in range(1, 14):
            deck.append(Card(i, 0))
        for i in range(1, 14):
            deck.append(Card(i, 1))
        for i in range(1, 14):
            deck.append(Card(i, 2))
        for i in range(1, 14):
            deck.append(Card(i, 3))
        return deck

    # כתיבה של החפיסה
    def __str__(self):
        return (f'i am {self.deck}')

    # ערבוב של החפיסה
    def _shuffle(self):
        if len(self.deck) <= 52:
            shuffle(self.deck)
        else:
            print('cant shuffle,count the cards!')

    # מחזירה את הקלף הראשון בחבילה
    def dealOne(self):
        if 53 > len(self.deck) > 0:
             return self.deck.pop(0)
        else:
            return ('count the cards')



    # מערבבת את החבילה ומסמנת את ראש החפיסה
    def new_Game(self):
        self._shuffle()
        return self.deck[0]

    # מדפיסה את החבילה
    def show(self):
        print(self.deck)

