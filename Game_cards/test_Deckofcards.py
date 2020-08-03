from unittest import TestCase
from Game_cards.Deckofcards import Deckofcards
from Game_cards.Card import Card


class TestDeckofcards(TestCase):
    def setUp(self):
        self.d1 = Deckofcards()
        self.d2 = Deckofcards()
        self.d3 = Deckofcards()
        self.d4 = ''

    def test_deck_has_52_cards(self):
        # Arrange
        d7 = Deckofcards()
        # Act
        # Assert
        self.assertEqual(len(d7.deck), 52)

    def test_shuffle(self):
        self.assertTrue(self.d1.shuffle() == True)
        self.d1.dealOne()
        self.assertTrue(self.d1.shuffle() == False)
        self.d3.shuffle()
        self.assertFalse(self.d3 != self.d2 == True)

    def test_deal_one(self):
        card = self.d1.deck[0]
        card1 = self.d1.dealOne()
        if card == card1:
            self.assertEqual((card, card1) == True)
        self.assertTrue(len(self.d1.deck) == 51)
        for i in range(51):
            self.d1.dealOne()
        self.assertTrue(len(self.d1.deck) == 0)

    def test_new_game(self):
        self.d1.newGame()
        self.assertTrue((self.d1 != self.d2) == True)
        self.d1.dealOne()
        self.assertTrue((self.d1 != self.d2) == True)

    def test_show(self):
        pass
