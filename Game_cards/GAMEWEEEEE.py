# הכנסת משתנים של השחקן

class Player:

    def __init__(self, name, sum1, card=53):
        self.list1 = []
        self.name = ''
        self.sum1 = sum1
        self.card = card


# מקבלת חבילת קלפים חדשה לשחקן
    def setHand(self, deck1):
        for i in range(self.card):
            if self.card < 53:
                return self.list1.append(deck1.dealOne())
            else:
                return False

p1=Player('KOBI',5000,53)
p1.setHand()

