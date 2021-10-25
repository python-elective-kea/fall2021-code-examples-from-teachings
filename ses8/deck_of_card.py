class Deck:
    def __init__(self):
        self.cards = ['A', 'K', '4', '7']

    def __getitem__(self, key):
        return self.cards[key]
