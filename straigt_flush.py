import numpy as np
from event import Event
from simulate import Simulator


class StraightFlush(Event):
    """ check if there is a straight flush at hand
        without considering wild cards
    """
    def __call__(self, d, cards):
        cards = d.reduce(cards)
        cards = d.unique(cards)
        cards = d.sort(cards)
        cards_dict = d.separate(cards)
        return False

    def consecutive(self, cards, stepsize=1):
        """ returns groups of consecutive arrays from cards
            >>> a = np.array([0, 47, 48, 49, 50, 97, 98, 99])
            >>> consecutive(a)

            >>> [array([0]), array([47, 48, 49, 50]), array([97, 98, 99])]
        """
        return np.split(cards, np.where(np.diff(cards) != stepsize)[0]+1)


def main():
    n_exp = 100000
    event = StraightFlush()
    simulator = Simulator(event)
    prob = simulator.simulate(n_exp)
    print('Number of experiments conducted: {}.'.format(n_exp))
    print('Probability of having a straight flush at hand: {:.4f}.'.format(prob))


if __name__ == '__main__':
    main()
