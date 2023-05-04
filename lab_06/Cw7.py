import random


def deal_cards():
    cards = [f"{fig} {col}" for fig in ["As", "Król", "Dama", "Walet", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
                              for col in ["pik", "kier", "karo", "trefl"]]
    random.shuffle(cards)
    players = {"Alan": [], "Maciek": [], "Jurek": [], "Kacper": []}
    for i in range(5):
        for player in players:
            karta = cards.pop()
            players[player].append(karta)

    for player, cards in players.items():
        print(f"{player}: {cards}")


deal_cards()
