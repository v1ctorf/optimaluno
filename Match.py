from Game import Game
from Player import Player

game = Game()

players = ["Alice", "Bob", "Charlie", "David"]

for player in players:
    game.addPlayer(Player(player))

game.deal()
game.show_all_players()

game.play()