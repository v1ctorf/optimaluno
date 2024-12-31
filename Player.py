from Card import Card
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.handCards = []


    def play(self, currentCard):
        print('- ' + self.name + ' is assessing ' + currentCard.color + ' ' + currentCard.value)
        print('- ' + self.name + '\'s hands', end=": ")
        for card in self.handCards:
            print(card.color + ' ' + card.value, end="; ")
        print('\n')

        playableCards = []

        for card in self.handCards:
            if card.color == currentCard.color or card.value == currentCard.value or card.color == 'W':
                playableCards.append(card)

        if not playableCards:
            return None
        
        card = playableCards.pop()
        self.handCards.remove(card)

        if card.color == 'W':
            colors = ['B', 'G', 'R', 'Y']
            card.chosenColor = random.choice(colors)
        else:
            card.chosenColor = card.color

        return card

