import numpy as np


class Deck(object):
    def __init__(self):
        # to represent 108 cards
        # 1-13: Spades 1-13; 14-26: Spades 1-13;
        # 27-39: Hearts 1-13; 40-52: Hearts 1-13;
        # 53-65: Diamonds 1-13; 66-78: Diamonds 1-13;
        # 79-91: Clubs 1-13; 92-104: Clubs 1-13;
        # 105,106: black jokers; 107,108: red jokers.
        self.deck = np.arange(1, 109, 1)

    def draw_cards(self, n_cards=27):
        return np.random.choice(self.deck, n_cards, replace=False)

    def reduce(self, cards):
        # map Spades
        cards = np.where((cards >= 14) * (cards <= 26), cards-13, cards)
        # map Hearts
        cards = np.where((cards >= 40) * (cards <= 52), cards-13, cards)
        # map Diamonds
        cards = np.where((cards >= 66) * (cards <= 78), cards-13, cards)
        # map Clubs
        cards = np.where((cards >= 92) * (cards <= 104), cards-13, cards)
        return cards

    def separate(self, cards):
        spades = cards[(cards >= 1) * (cards <= 26)]
        hearts = cards[(cards >= 27) * (cards <= 52)]
        diamonds = cards[(cards >= 53) * (cards <= 78)]
        clubs = cards[(cards >= 79) * (cards <= 104)]
        jokers = cards[(cards >= 105) * (cards <= 106)]
        cards_dict = {'spades': spades, 'hearts': hearts,
                      'diamonds':diamonds, 'clubs': clubs, 'jokers': jokers}
        return cards_dict

    def sort(self, cards):
        return np.sort(cards)

    def get_full_deck(self):
        return self.deck
