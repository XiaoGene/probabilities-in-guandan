import time
import numpy as np
from event import Event
from simulator import Simulator


class StraightFlush(Event):
    """ check if there is a straight flush at hand
        without considering wild cards
    """
    def __call__(self, d, cards):
        cards = d.reduce(cards)
        cards = d.unique(cards)
        cards = d.sort(cards)
        cards_dict = d.separate(cards)
        cards_dict = d.collapse(cards_dict)
        for key in cards_dict.keys():
            if key == 'jokers':
                continue
            suit_cards = cards_dict[key]
            if len(suit_cards) >= 5:
                for i in range(len(suit_cards)-4):
                    if self.is_consecutive(suit_cards[i:i+5]):
                        return True
                if self.contain_10jqka(suit_cards):
                    return True
        return False

    def is_consecutive(self, array, stepsize=1):
        """ returns true if array is 5-consecutive numbers
        """
        return (np.diff(array) != stepsize).all()

    def contain_10jqka(self, suit_cards):
        target_cards = np.array([10, 11, 12, 13, 1])
        return np.isin(target_cards, suit_cards).all()


def main():
    n_exp = 1000000
    event = StraightFlush()
    simulator = Simulator(event, n_exp)
    start = time.time()
    prob = simulator.simulate()
    end = time.time()
    ellapsed_time = end - start
    print('Number of experiments conducted: {}.'.format(n_exp))
    print('Time taken: {:.0f}[min] {:.2f}[s].'.format(ellapsed_time // 60, ellapsed_time % 60))
    print('Probability of having a straight flush at hand: {:.4f}.'.format(prob))


if __name__ == '__main__':
    main()
