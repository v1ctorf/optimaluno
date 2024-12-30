from Card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.handCards = []


    def play(self, currentCard):
        # print(self.name + 'is assessing ' + currentCard.color + ' ' + currentCard.value)

        card = self.handCards.pop(0)
        return card

