from Game_cards.Card import Card
from random import shuffle


class Deckofcards:

    # איניט של חפיסת קלפים שלמה עפ הסוגים
    def __init__(self):
        self.deck=[]
        for i in range (1,14):
            self.deck.append(Card(i,0))
        for i in range(1,14):
            self.deck.append(Card(i,1))
        for i in range (1,14):
            self.deck.append(Card(i,2))
        for i in range (1,14):
            self.deck.append(Card(i,3))


    # כתיבה של החפיסה
    def __str__(self):
        return (f'i am {self.deck}')

    #ערבוב של החפיסה
    def shuffle(self):
        if len(self.deck) == 52:
            shuffle(self.deck)
            return True
        else:
            print('cant shuffle')
            return  False

    # מחזירה את הקלף הראשון בחבילה
    def dealOne(self):
        if len(self.deck)>0:
            return self.deck.pop(0)


    #מערבבת את החבילה
    def newGame(self):
        self.__init__()
        self.shuffle()

    # מדפיסה את החבילה
    def show(self):
        return (self.deck)

# d1=Deckofcards()
# print(d1)
# d1.shuffle()
# print(d1)
# d1.dealOne()
# print(d1)
# d1.newGame()
# print(d1)
# d1.show()


