# 计算一局掼蛋中同花顺出现在某一家的概率
# 同花顺：花色相同的五张相邻的单张

import numpy as np
from deck import Deck


def is_straight_flush(cards):
    assert(cards.shape[0] == 27)


def main():
    d = Deck()
    cards = d.draw_cards()
    cards = d.reduce(cards)
    cards = d.sort(cards)
    cards_list = d.separate(cards)


if __name__ == '__main__':
    np.set_printoptions(precision=3, linewidth=1000, suppress=False)
    main()
