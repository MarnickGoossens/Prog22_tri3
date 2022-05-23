from oorlog import *

spelers = 4

game = Game(spelers)
deck = game.maak_deck()
print(deck)
deck = game.shuffle_deck(deck)
print(deck)
