from Card import Card
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.handCards = []


    def play(self, currentCard):
        # print(self.name + ' is assessing ' + currentCard.color + ' ' + currentCard.value, end="\n\n")

        card = self.handCards.pop(0)

        if card.color == 'W':
            colors = ['B', 'G', 'R', 'Y']
            card.chosenColor = random.choice(colors)
        else:
            card.chosenColor = card.color

        return card

