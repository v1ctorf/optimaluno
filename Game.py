from Deck import Deck
from Player import Player

# deck = Deck()
# deck.show_all_cards()

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []

    def deal(self):
        for i in range(7):
            for player in self.players:
                player.handCards.append(self.deck.dealCard())

    def addPlayer(self, player):
        self.players.append(player)
        return self

    def show_all_players(self):
        for player in self.players:
            print(player.name)
            for card in player.handCards:
                print(card.color, card.value)


game = Game()
game.addPlayer(Player("Alice"))
game.addPlayer(Player("Bob"))
game.deal()

game.show_all_players()