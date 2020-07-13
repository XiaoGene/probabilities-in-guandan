from event import Event
from simulator import Simulator


class ContainTwoSpadeOnes(Event):
    """ check if there are two Spade 1's at hand
    """
    def __call__(self, d, cards):
        if 1 in cards and 14 in cards:
            return True
        else:
            return False


def main():
    n_exp = 10000
    event = ContainTwoSpadeOnes()
    simulator = Simulator(event)
    prob = simulator.simulate(n_exp)
    print('Number of experiments conducted: {}.'.format(n_exp))
    print('Probability of having two Spade 1 at hand: {:.4f}.'.format(prob))

if __name__ == '__main__':
    main()
