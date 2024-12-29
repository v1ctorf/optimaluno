from Card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.handCards = []


    def assessHand(self):
        self.handCards.sort(key=lambda x: x.value)
        self.handCards.sort(key=lambda x: x.color)
        return self.handCards


    def play(self):
        card = self.handCards.pop(0)
        return card

