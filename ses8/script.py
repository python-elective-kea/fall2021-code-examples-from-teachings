class A:
    def __init__(self):
        self.name = 'Claus'


    def __len__(self):
        return len(self.name)


    def __add__(x, y):
        return x.name + y.name

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return self.name
