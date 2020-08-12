from Game_cards.Deckofcards import Deckofcards
from Game_cards.Card import Card
from random import shuffle


class Player:

    # הכנסת משתנים של השחקן
    def __init__(self, name, sum1, numofcards=5):
        self.list1 = []
        self.name = name
        self.sum1 = sum1
        self.numofcards = numofcards

    # מקבלת חבילת קלפים חדשה לשחקן
    def setHand(self, deck1):
        if self.numofcards <= len(deck1.deck):
            for i in range(self.numofcards):
                self.list1.append(deck1.dealOne())

    # מושכת קלף אקראי מהשחקן
    def getCard(self):
        if len(self.list1) > 0:
            shuffle(self.list1)
            return self.list1.pop(0)

    # מוסיף קלף לשחקן
    def addCard(self, card1):
        if type (card1)==int:
            if 0<card1<14:
                self.list1.append(card1)
            else:
                return ('need legal card')
        else:
            return ('need card')
    # מוריד סכום כסף מהשחקן
    def reduceAmount(self, amount):
        if type(amount) == int:
            if amount<0:
                amount=0
                self.sum1 -= amount
            else:
                self.sum1 -= amount
        else:
            return 'error,need number'

    # מוסיף כמות כסף לשחקן
    def addAmount(self, amount):
        if type(amount) == int:
            if amount<0:
                amount=0
                self.sum1 += amount
            else:
                self.sum1 += amount
        else:
            return 'error,need number'

    # הדפסה של השחקן עם ערכים
    def __repr__(self):
        return f'i am {self.name} and i have {self.sum1}money my cards :{self.list1}'

