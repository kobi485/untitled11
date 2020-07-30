from unittest import TestCase
from Game_cards.Deckofcards import Deckofcards


class TestDeckofcards(TestCase):
    def setUp(self):
        self.d1=Deckofcards()

    def test_shuffle(self):
        self.assertTrue(self.d1.shuffle() == True)
        self.d1.dealOne()
        self.assertTrue(self.d1.shuffle() == False)



    def test_deal_one(self):
        self.d1.dealOne()
        self.assertTrue(len(self.d1.deck)==51)
        for i in range (51):
            self.d1.dealOne()
        self.assertTrue(len(self.d1.deck)==0)


    def test_new_game(self):
        pass

    def test_show(self):
        pass
