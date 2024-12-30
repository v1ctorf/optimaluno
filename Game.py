from Deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.discards = []
        self.direction = 1  # 1 for forward, -1 for reverse

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
                print(card.color + " " + card.value, end=", ")
            print("\n")

    def log(self, player=None, card=None):
        if not player:
            print("First card is " + card.color + " " + card.value)
        else:
            print(player.name + " plays " + card.color + " " + card.value)
        
        print("distribution:", end=" ")

        for player in self.players:
            print(player.name + ": " + str(len(player.handCards)), end=" | ")

        print("deck: " + str(len(self.deck.cards)), end=" | ")
        print("discards: " + str(len(self.discards)), end=" | ")
        print("chosen colour: " + card.chosenColor, end="\n\n")

    def checkWin(self):
        for player in self.players:
            if not player.handCards:
                print(player.name + " wins!")
                return True
        return

    def play(self):
        current_index = 0
        nextPlayerMustSkip = False
        color = None

        while self.deck.cards:
            if not self.discards:
                turn = self.deck.cards.pop()
                self.discards.append(turn)
                turn.chosenColor = turn.color
                color = turn.chosenColor
                # TODO: handle if first card is a wild card
                nextPlayerMustSkip = turn.value == 'skip'

                if turn.value == 'reverse':
                    self.direction *= -1

                self.log(None, turn)
                continue

            currentCard = self.discards[-1]

            if nextPlayerMustSkip:
                current_index = (current_index + self.direction) % len(self.players)
                nextPlayerMustSkip = False
                continue

            player = self.players[current_index]
            turn = player.play(currentCard)
            self.log(player, turn)
            self.discards.append(turn)
            colour = turn.chosenColor

            if turn.value == 'skip':
                nextPlayerMustSkip = True
            elif turn.value == 'reverse':
                self.direction *= -1

            if self.checkWin():
                self.deck.cards = []
                break

            if not self.deck.cards:
                raise Exception("No more cards in deck!")

            current_index = (current_index + self.direction) % len(self.players)

        print("Game over!")
