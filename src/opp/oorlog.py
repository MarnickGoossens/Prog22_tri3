from random import shuffle, choice


class Game:
    def __init__(self, spelers):
        self.spelers = spelers

    def draai_kaarten(self):
        print()
        for speler, kaarten in self.spelers.items():
            print(f"{speler}:   {kaarten[0]}")

    def check_kaarten(self):
        open_kaarten_speler = []
        winner = None
        for speler, kaarten in self.spelers.items():
            if kaarten[0][0] == "J":
                kaart = ((11, kaarten[0][1]), speler)
                open_kaarten_speler.append(kaart)
                spelers[speler].remove(kaarten[0])
            elif kaarten[0][0] == "Q":
                kaart = ((12, kaarten[0][1]), speler)
                open_kaarten_speler.append(kaart)
                spelers[speler].remove(kaarten[0])
            elif kaarten[0][0] == "K":
                kaart = ((13, kaarten[0][1]), speler)
                open_kaarten_speler.append(kaart)
                spelers[speler].remove(kaarten[0])
            elif kaarten[0][0] == "A":
                kaart = ((14, kaarten[0][1]), speler)
                open_kaarten_speler.append(kaart)
                spelers[speler].remove(kaarten[0])
            else:
                open_kaarten_speler.append((kaarten[0], speler))
        open_kaarten = []
        for i in open_kaarten_speler:
            open_kaarten.append(i[0])
        hoogste_kaart = max(open_kaarten)
        for i in open_kaarten_speler:
            if hoogste_kaart in i:
                winner = i[1]
        for kaart in open_kaarten:
            for speler, kaarten in spelers.items():
                if kaart in kaarten:
                    kaarten.remove(kaart)
        spelers[winner].extend(open_kaarten)
        return winner


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

    def shuffle_deck(self):
        shuffle(self.deck)
        return self.deck

    def maak_spelers(self, aantal_spelers):
        dictionary = {}
        for i in range(1, aantal_spelers + 1):
            speler = "speler" + str(i)
            cards = []
            for j in range(int(52 / aantal_spelers)):
                card = choice(self.deck)
                self.deck.remove(card)
                cards.append(card)
            dictionary[speler] = cards
        return dictionary


# aantal_spelers = int(input(f"hoeveel spelers\n"))
aantal_spelers = 4
deck = Deck()
deck.maak_deck()
deck.shuffle_deck()
spelers = deck.maak_spelers(aantal_spelers)

game = Game(spelers)
game.draai_kaarten()
winner = game.check_kaarten()
print(f"\n{winner} wint")
game.draai_kaarten()
winner = game.check_kaarten()
print(f"\n{winner} wint")
game.draai_kaarten()
winner = game.check_kaarten()
print(f"\n{winner} wint")

print()
for speler, kaarten in spelers.items():
    print(len(kaarten))
