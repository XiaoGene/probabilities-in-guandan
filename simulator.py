import random
import numpy as np
from deck import Deck
import multiprocessing as mp


class Simulator(object):
    def __init__(self, event):
        """ Args:
                event(event.Event): indicator function to check
                    whether an event happend given cards
        """
        self.d = Deck()
        self.event = event

    def set_seed(self, seed=0):
        random.seed(seed)

    def _simulate(self, n_exp):
        n_positive = 0
        for _ in range(n_exp):
            cards = self.d.draw_cards()
            if self.event(self.d, cards):
                n_positive += 1
        prob = float(n_positive) / n_exp
        return prob

    def simulate(self, n_exp, n_processes=None):
        if n_processes is None:
            n_processes = mp.cpu_count()
        if n_processes == 1:
            prob = self._simulate(n_exp)
        else:
            n_exp_per_process = int(np.ceil(n_exp/n_processes))
            n_exp_list = [n_exp_per_process for _ in range(n_processes-1)]
            n_exp_list.append(n_exp - n_exp_per_process*(n_processes-1))
            pool = mp.Pool(n_processes)
            prob_list = pool.map(self._simulate, n_exp_list)
            prob = np.mean(np.array(prob_list))
        return prob
            
