import time
from event import Event
from simulator import Simulator


class ContainFourJokers(Event):
    """ check if there are four jokers at hand
    """
    def __call__(self, d, cards):
        if 105 in cards and 106 in cards and 107 in cards and 108 in cards:
            return True
        else:
            return False


def main():
    n_exp = 1000000
    event = ContainFourJokers()
    simulator = Simulator(event, n_exp)
    start = time.time()
    prob = simulator.simulate()
    end = time.time()
    ellapsed_time = end - start
    print('Number of experiments conducted: {}.'.format(n_exp))
    print('Time taken: {:.0f}[min] {:.2f}[s].'.format(ellapsed_time // 60, ellapsed_time % 60))
    print('Probability of having four jokers at hand: {:.4f}.'.format(prob))

if __name__ == '__main__':
    main()
