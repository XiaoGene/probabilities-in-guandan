from deck import Deck
import numpy as np


def test_reduce():
    d = Deck()
    cards_deck = d.get_full_deck()
    cards_reduced = d.reduce(cards_deck)
    spades = np.arange(1, 14)
    hearts = spades + 26
    diamonds = hearts + 26
    clubs = diamonds + 26
    jokers = np.array([105, 106, 107, 108])
    cards_target = np.concatenate((
        spades, spades, hearts, hearts,
        diamonds, diamonds, clubs, clubs, jokers
    ))
    print(cards_reduced - cards_target)
    assert(np.sum(np.absolute(cards_reduced-cards_target)) < 1e-6)


def test_collapse():
    d = Deck()
    cards_deck = d.get_full_deck()
    cards_deck = d.reduce(cards_deck)
    cards_deck = d.unique(cards_deck)
    cards_dict = d.separate(cards_deck)
    cards_dict = d.collapse(cards_dict)
    spades = np.arange(1, 14)
    cards_dict_target = {
        'spades': spades, 'hearts': spades,
        'diamonds': spades, 'clubs': spades,
        'jokers': np.array([105, 106, 107, 108])
    }
    for key in cards_dict_target.keys():
        print(key, cards_dict_target[key] - cards_dict[key])
        assert(np.sum(np.absolute((cards_dict_target[key]-cards_dict[key]))) < 1e-6)
