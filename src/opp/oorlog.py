from random import shuffle


class Deck:
    def __init__(self):
        self.deck = []

    def maak_deck(self):
        kaart_reeks = ["A"] + list(range(2, 11)) + ["J", "Q", "K"]
        kaart_kleuren = ["♠", "♥", "♦", "♣"]
        self.deck = []

        for kaart_kleur in kaart_kleuren:
            for kaart_index in range(len(kaart_reeks)):
                self.deck.append((kaart_reeks[kaart_index], kaart_kleur))
        return self.deck

    def shuffle_deck(self, deck):
        print(shuffle(deck))
        return shuffle(deck)


class Game:
    def __init__(self, spelers):
        self.deck = []
        self.spelers = spelers

    def maak_deck(self):
        kaart_reeks = ["A"] + list(range(2, 11)) + ["J", "Q", "K"]
        kaart_kleuren = ["♠", "♥", "♦", "♣"]
        self.deck = []

        for kaart_kleur in kaart_kleuren:
            for kaart_index in range(len(kaart_reeks)):
                self.deck.append((kaart_reeks[kaart_index], kaart_kleur))
        return self.deck

    def shuffle_deck(self, deck):
        print(shuffle(deck))
        return shuffle(deck)
