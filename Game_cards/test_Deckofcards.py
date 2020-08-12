from unittest import TestCase
from Game_cards.Deckofcards import Deckofcards
from Game_cards.Card import Card
from Game_cards.Player import Player


class TestDeckofcards(TestCase):
    def setUp(self):
        # הגדרה של משתנים לבדיקות
        self.d1 = Deckofcards()
        self.d2 = Deckofcards()
        self.d3 = Deckofcards()
        self.d4 = ''

    def test_deck_has_52_cards(self):
        # בדיקה האם יש בחבילה 52 קלפים
        d7 = Deckofcards()
        self.assertEqual(len(d7.deck), 52)

    def test_shuffle(self):
        # בדיקה האם אחרי ערבוב יש לנו עדין 52 קלפים או מספר נתון של קלפים בחבילה
        d8=Deckofcards()
        d8._shuffle()
        self.assertEqual(len(d8.deck), 52)


    def test_shuffle1(self):
        # בדיקה האם אחרי ערבוב יש לנו עדין 52 קלפים או מספר נתון של קלפים בחבילה
        d8=Deckofcards()
        d8._shuffle()
        self.assertNotEqual(len(d8.deck), 51)


    def test_shuffle2(self):
        # בדיקה האם אחרי ערבוב יש לנו עדין 52 קלפים או מספר נתון של קלפים בחבילה
        d8 = Deckofcards()
        d8._shuffle()
        self.assertNotEqual(len(d8.deck), 53)


    def test_shuffle3(self):
        #בדיקה האם המתודה מבצעת ערבוב לחבילה שאינה מלאה

        d8=Deckofcards()

        d8.dealOne()
        self.assertTrue(d8._shuffle()=='cant shuffle,count the cards!')



    def test_deal_one(self):
        # בדיקה המראה שהמתודה אכן מוציאה את הקלף מראש החפיסה
        card = self.d1.deck[0]
        card1 = self.d1.dealOne()
        if card == card1:
            self.assertEqual(card, card1)

    def test_deal_one1(self):
        # המתודה אכן מוציאה קלף 1 בלבד
        d1=Deckofcards()
        d1.dealOne()
        self.assertEqual(len(d1.deck) , 51)

    def test_deal_one2(self):
        #כשאר מפעילים אותה מספר פעמיים
        d1 = Deckofcards()
        d1.dealOne()
        for i in range(51):
            d1.dealOne()
        self.assertTrue(len(d1.deck) == 0)

    def test_deal_one3(self):
        # מה קורה אם מגיעה חבילת קלפים "שאיכשהו" לא עומדת בקריטריונים (נוכלים)
        for i in range(100):
            self.d1.deck.append(i)
        self.assertEqual(self.d1.dealOne(),'count the cards')



    def test_new_game(self):
        # בדיקה האם המתודה אכן מקבלת חבילה ומערבבת אותה
        self.d1.new_Game()
        self.assertTrue((self.d1 != self.d2) == True)


    def test_show(self):
       self.d1.show()

