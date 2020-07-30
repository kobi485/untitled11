from Game_cards import Card
from Game_cards.Deckofcards import Deckofcards
from Game_cards.Player import Player
from random import randint
from random import shuffle

class CardGame:

    # מספר הקלפים לכל שחקן+שחקנים
    def __init__(self,cardnumber):
        self.cardnumber = cardnumber
        self.deck = Deckofcards()
        self.player = []
        for i in range(4):
            self.player.append(Player(input('enter name:'),randint(5000,10000),self.cardnumber))
    #וחלוקה של קלפים ערבוב של החפיסה מחדש
    def newGame(self):
        self.deck.shuffle()
        for i in self.player:
            i.setHand(self.deck)

    def __str__(self):
        return (f'{self.player[0]}\n{self.player[1]}\n{self.player[2]}\n{self.player[3]}')





cardgame=CardGame(5)
cardgame.newGame()
print(cardgame)
