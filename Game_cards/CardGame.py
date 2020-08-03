from Game_cards import Card
from Game_cards.Deckofcards import Deckofcards
from Game_cards.Player import Player
from random import randint
from random import shuffle

class CardGame:



    # מספר הקלפים לכל שחקן+שחקנים
    def __init__(self,cardnumber=5):
        self.deck = Deckofcards()
        self.players = []
        self.cardnumber=cardnumber

        if type (cardnumber) != int:
            cardnumber==5
        if cardnumber>13:
            cardnumber==13
        if cardnumber<1:
            cardnumber==5
        hag=randint(5000,10000)

        for i in range(4):
            self.players.append(Player(input('enter name:'),hag,self.cardnumber))


    #וחלוקה של קלפים ערבוב של החפיסה מחדש
    def newGame(self):
        self.deck.newGame()
        shuffle(self.deck)
        for i in self.players:
            i.setHand(self.deck)



    def __str__(self):
        return (f'{self.players[0]}\n{self.players[1]}\n{self.players[2]}\n{self.players[3]}')






cardgame=CardGame(5)
