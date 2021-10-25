class Deck:
    def __init__(self):
        self.cards = ['A', 'K', '4', '7']

    def __getitem__(self, key):
        return self.cards[key]
    
    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del(self.cards[key])

    def msg(self, x):
        print(x)
