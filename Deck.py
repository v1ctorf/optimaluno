from Card import Card
import random

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()


    def build(self):
        with open('cards.csv', 'r') as f:
            for line in f:
                card = line.strip().split(',')
                if card[3] == '1':
                    new_card = Card(card[0], card[1], card[2])
                    self.cards.append(new_card)


    def shuffle(self):
        random.shuffle(self.cards)
    

    def show_all_cards(self):
        for card in self.cards:
            print(card.color, card.value)


    def dealCard(self):
        if not self.cards:
            raise Exception('Deck is empty')
        
        return self.cards.pop() if len(self.cards) > 0 else None