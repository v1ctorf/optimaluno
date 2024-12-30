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
    

    def log(self, turn_no, player=None, card=None):
        print(str(turn_no), end=") ")

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
        turn_no = 1

        while self.deck.cards:            
            if not self.discards:
                turn = self.deck.cards.pop()
                self.discards.append(turn)
                self.log(turn_no, None, turn)
                continue

            for player in self.players:
                turn_no = turn_no + 1
                turn = player.play()
                self.discards.append(turn)
                self.log(turn_no, player, turn)

                if self.checkWin():
                    self.deck.cards = []
                    break
                
                if not self.deck.cards:
                    raise Exception("No more cards in deck!")
        
        print("Game over!")