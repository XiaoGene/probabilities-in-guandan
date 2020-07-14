import random
from deck import Deck


class Simulator(object):
    def __init__(self, event, n_exp):
        """ Args:
                event(event.Event): indicator function to check
                    whether an event happend given cards
        """
        self.d = Deck()
        self.event = event
        self.n_exp = n_exp

    def set_seed(self, seed=0):
        random.seed(seed)

    def simulate(self):
        n_positive = 0
        for _ in range(self.n_exp):
            cards = self.d.draw_cards()
            if self.event(self.d, cards):
                n_positive += 1
        prob = float(n_positive) / self.n_exp
        return prob
