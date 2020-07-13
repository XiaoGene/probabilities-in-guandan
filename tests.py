from deck import Deck
import numpy as np


def test_reduce():
    d = Deck()
    cards_deck = d.get_full_deck()
    cards_mapped = d.map(cards_deck)
    spades = np.arange(1, 14)
    hearts = spades + 26
    diamonds = hearts + 26
    clubs = diamonds + 26
    jokers = np.array([105, 106, 107, 108])
    cards_target = np.concatenate((
        spades, spades, hearts, hearts,
        diamonds, diamonds, clubs, clubs, jokers
    ))
    print(cards_mapped - cards_target)
    assert(np.sum(np.absolute(cards_mapped-cards_target)) < 1e-6)
