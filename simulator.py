import numpy as np
from deck import Deck


class Simulator(object):
    def __init__(self, event):
        """ Args:
                event(event.Event): indicator function to check
                    whether an event happend given cards
        """
        self.d = Deck()
        self.event = event

    def set_seed(self, seed=0):
        np.random.seed(seed)

    def simulate(self, n_exp=10):
        n_positive = 0
        for _ in range(n_exp):
            cards = self.d.draw_cards()
            if self.event(self.d, cards):
                n_positive += 1
        prob = float(n_positive) / n_exp
        return prob
