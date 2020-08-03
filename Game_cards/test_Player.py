from unittest import TestCase
from Game_cards.Player import Player
from Game_cards.Deckofcards import Deckofcards


class TestPlayer(TestCase):
    def setUp(self):
        self.player1 = Player('KOBI', 5000, 10)
        self.player2 = Player(3000, 3000, 5)
        self.player3 = Player('kboi', 10000, 5)

    def test_set_hand(self):
        deck1 = Deckofcards()
        self.player1.setHand(deck1)
        self.assertEqual(len(self.player1.list1), self.player1.numofcards)

    def test_no_cards(self):
        # Arrange
        deck1 = Deckofcards()
        for i in range(49):
            deck1.deck.pop(0)
        # Act
        self.player3.setHand(deck1)
        # Assert
        self.assertFalse(self.player3.list1)

    def test_get_card(self):
       player=Player('kobi',5000)
       player.getCard()
       self.assertTrue(len(player.list1)==0)

       player1=Player('avi',5000,5)
       deck=Deckofcards()
       player1.setHand(deck)
       player1.getCard()
       self.assertTrue(len(player1.list1),6)



    def test_add_card(self):
        player1=Player('kobi',5000,5)
        deck1=Deckofcards()
        player1.setHand(deck1)
        player1.getCard()
        self.assertTrue(len(player1.list1),4)



    def test_add_amount(self):
        player1 = Player('kobi', 5000, 5)
        player1.addAmount(3000)
        self.assertTrue(player1.sum1== 8000)

    def test_add_amount1(self):
        player2 = Player('kobi', 0, 5)
        player2.addAmount(7500)
        self.assertTrue(player2.sum1== 7500)

    def test_add_amount2(self):

        player3 = Player('koko', -2500, 10)
        player3.addAmount(10000)
        self.assertTrue(player3.sum1==7500)

    def test_reduce_amount(self):

        player1 = Player('kobi', 5000, 5)
        player1.reduceAmount(3000)
        self.assertTrue(player1.sum1==2000)

    def test_reduce_amount1(self):

        player2 = Player('kobi', 0, 5)
        player2.reduceAmount(7500)
        self.assertTrue(player2.sum1==-7500)

    def test_reduce_amount2(self):
        player3 = Player('koko',12500, 10)
        player3.reduceAmount(10000)
        self.assertTrue(player3.sum1==2500)

