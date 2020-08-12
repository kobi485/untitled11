from unittest import TestCase
from Game_cards.Player import Player
from Game_cards.Deckofcards import Deckofcards


class TestPlayer(TestCase):
    # הצבה של משתנים לבדיקות
    def setUp(self):
        self.player1 = Player('KOBI', 5000, 10)
        self.player2 = Player(3000, 3000, 5)
        self.player3 = Player('kboi', 10000, 5)


    # בדיקה האם השחקן אכן מקבל חבילה חדשה ליד
    def test_set_hand(self):
        deck1 = Deckofcards()
        self.player1.setHand(deck1)
        self.assertEqual(len(self.player1.list1), self.player1.numofcards)


    # בדיקה האם השחקן מקבל קלפים כאשר אין מספיק קלפים בחבילה
    def test_no_cards(self):
        deck1 = Deckofcards()
        for i in range(49):
            deck1.deck.pop(0)
        self.player3.setHand(deck1)
        self.assertFalse(self.player3.list1)


    # האם המתודה משכה קלף כאשר אין לשחקן קלפים
    def test_get_card(self):
       player=Player('kobi',5000)
       player.getCard()
       self.assertTrue(len(player.list1)==0)


    # בדיקה האם המתודה משכה קלף מהשחקן
    def test_get_card2(self):
       player1=Player('avi',5000,5)
       deck=Deckofcards()
       player1.setHand(deck)
       player1.getCard()
       self.assertEqual(len(player1.list1),4)


    #בדיקה האם המתודה הוסיפה קלף לשחקן
    def test_add_card(self):
        player1=Player('kobi',5000,5)
        deck1=Deckofcards()
        player1.setHand(deck1)
        player1.addCard(6)
        self.assertEqual(len(player1.list1),6)


    #בדיקה האם אכן מוסיפים קלף לשחקן ולא משהו אחר
    def test_add_card2(self):
        player1=Player('kobi',5000,5)
        deck1=Deckofcards()
        player1.setHand(deck1)
        player1.getCard()
        self.assertEqual(player1.addCard('kobi'),'need card')


    #בדיקה האם הקלף שרוצים להוסיף אכן תקין
    def test_add_card3(self):
        player1 = Player('kobi', 5000, 5)
        deck1 = Deckofcards()
        player1.setHand(deck1)
        self.assertEqual(player1.addCard(20),'need legal card')



    #האם המתודה מוסיפה כסף
    def test_add_amount(self):
        player1 = Player('kobi', 5000, 5)
        player1.addAmount(3000)
        self.assertTrue(player1.sum1== 8000)


    #האם היא תוסיף כסף לשחקן בלי כסף בכיס
    def test_add_amount1(self):
        player2 = Player('kobi', 0, 5)
        player2.addAmount(7500)
        self.assertTrue(player2.sum1== 7500)


    #בדיקה שמראה שהמתודה מתמודדת עם ערכים שאינם כסף
    def test_add_amount2(self):
        player3 = Player('koko',-2500 , 10)
        self.assertEqual(player3.addAmount('kobi'),'error,need number')


    #בדיקה שמרא שהמתודה עושה רק את הפעולה שהיא צריכה לבצע ולא יכולה להוריד כסף מסכום השחקן
    def test_add_amount3(self):
        player1 = Player('kobi', 5000, 5)
        player1.addAmount(-4000)
        self.assertTrue(player1.sum1 == 5000)


    #בדיקה שמראה שהמתודה אכן מורידה כסף
    def test_reduce_amount(self):
        player1 = Player('kobi', 5000, 5)
        player1.reduceAmount(3000)
        self.assertTrue(player1.sum1==2000)


    #מתודה שמראה שהשחקן יכול להיכנס למינוס
    def test_reduce_amount1(self):
        player2 = Player('kobi', 0, 5)
        player2.reduceAmount(7500)
        self.assertTrue(player2.sum1==-7500)

    #בדיקה שמראה איך המתודה מתמודדת עם הכנסה של משתנים שאינם תקינים ושהיא צריכה לקבל רק "כסף"
    def test_reduce_amount2(self):
        player3 = Player('koko',12500, 10)
        self.assertEqual(player3.reduceAmount('kobi'),'error,need number')

    #בדיקה שמראה שהמתודה מתמודדת עם חיסור של כסף ואם מביאים ערך שהוא מינוס אז היא מאפסת את עצמה ולא מורידה כסףף
    def test_reduce_amount3(self):
        player1 = Player('kobi', 5000, 5)
        player1.reduceAmount(-3000)
        self.assertTrue(player1.sum1==5000)

