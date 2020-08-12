from unittest import TestCase
from unittest.mock import patch
from Game_cards.CardGame import CardGame

from Game_cards.Deckofcards import Deckofcards
from Game_cards.Player import Player
from random import randint
from random import shuffle


class TestCardGame(TestCase):

# בודק מקרה קצה בו שמנו מספר מסויים של קלפים
    def test_init(self):
            self.card1=CardGame('s' 'w' 'q' 'y' , 13)
            self.assertEqual(self.card1.cardnumber,13)


#בודקת שהמתודה אכן מכניסה את השמות לרשימת השחקנים
    def test_init1(self):
            self.card1=CardGame(('s','w', 'q', 'y', 'k') , 13)
            self.assertEqual(self.card1.names,('s','w', 'q', 'y', 'k'))


#בדיקה המראה כיצד המתודה פועלת עם מקרים של ערכים לא תקינים
    def test_init2(self):
            self.card1=CardGame(('s','w', 'q', 'y') ,450)
            self.assertEqual(self.card1.cardnumber,13)


#בדיקה המראה כיצד המתודה פועלת עם ערכים שליילים במספר הקלפים אשר צריכים לחלק
    def test_init3(self):
            self.card1 = CardGame(('s', 'w', 'q', 'y'), -3)
            self.assertEqual(self.card1.cardnumber, 5)

#בדיקה האם המתודה מחזירה קלפים ומבצעת חלוקה לשחקנים
    def test_newGame(self):
        d=Deckofcards()
        with patch('Game_cards.Deckofcards.Deckofcards.new_Game',return_value=d) as mock1:
            # self.card1 = CardGame(('s', 'w', 'q', 'y'), 10)
            # self.card2=CardGame(('s', 'w', 'q', 'y'), 10)
            # gamecards1=self.card1.newGame()
            # self.assertEqual(self.card1.deck.show(), gamecards1)
            game=CardGame(('s', 'w', 'q', 'y'), 10)
            print(game.players)

#dick




