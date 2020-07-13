class Event(object):
    """ Interface for checking whether an event happens
    """
    def __call__(self, d, cards):
        """ Args:
                d(deck.Deck)
                cards(np.array): array of cards
            Returns:
                event_happend(bool): indicates whether this event happend for given cards
        """
        raise NotImplementedError
