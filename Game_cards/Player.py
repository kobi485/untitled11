from Game_cards.Deckofcards import Deckofcards
from Game_cards.Card import Card
from random import shuffle


class Player:

    # הכנסת משתנים של השחקן
    def __init__(self,name,sum1,card=5):
        self.list1=[]
        self.name=name
        self.sum1=sum1
        self.card=card

    # מקבלת חבילת קלפים חדשה לשחקן
    def setHand(self,deck1):
        for i in range(self.card):
            self.list1.append(deck1.dealOne())
    # מושכת קלף אקראי מהשחקן
    def getCard(self):
        if len(self.list1) > 0:
            shuffle(self.list1)
            return (self.list1.pop(0))
    # מוסיף קלף לשחקן
    def addCard(self,card1):
        self.list1.append(card1)
    # מוריד סכום כסף מהשחקן
    def reduceAmount(self,amount):
        self.sum1-=amount

    # מוסיף כמות כסף לשחקן
    def addAmount(self,amount):
        if type(amount)==int:
            self.sum1+=amount
        else:
            return ('error,nees number')

    #הדפסה של השחקן עם ערכים
    def __repr__(self):
        return (f'i am {self.name} and i have {self.sum1}money my cards :{self.list1}')




# d=Deckofcards()
# d.shuffle()
# player1=Player(100,5000)
# player1.setHand(d)
# player1.getCard()
# player1.addCard(d.deck[0])





