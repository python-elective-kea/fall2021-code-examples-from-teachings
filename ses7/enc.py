class Person:
    def __init__(self, name):
        self.name = name # public variable -> property
        self.__age = 23
        self.__children = []

    @property
    def name(self):
        return 'Peter' #self.__name

    @name.setter
    def name(self, name):
        if type(name) != str:
            print('Nop no no')
        else:
            self.__name = name

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, name):
        self.__children.append(name)









    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age


