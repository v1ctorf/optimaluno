from Deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.discards = []


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
        print("discards: " + str(len(self.discards)), end="\n\n")


    def checkWin(self):
        for player in self.players:
            if not player.handCards:
                print(player.name + " wins!")
                return True
        return


    def play(self):
        while self.deck.cards:    
            if not self.discards:
                turn = self.deck.cards.pop()
                self.discards.append(turn)
                
                nextPlayerMustSkip = turn.value == 'skip'

                self.log(None, turn)
                continue

            if len(self.discards) >= 1:
                currentCard = self.discards[-1]

            for player in self.players:
                if nextPlayerMustSkip:
                    nextPlayerMustSkip = False
                    continue
                
                turn = player.play(currentCard)
                self.log(player, turn)
                self.discards.append(turn)

                if turn.value == 'skip':
                    # print(player.name + ' forces next player to skip', end="\n\n")
                    nextPlayerMustSkip = True

                if self.checkWin():
                    self.deck.cards = []
                    break
                
                if not self.deck.cards:
                    raise Exception("No more cards in deck!")
        
        print("Game over!")