class Person:
   
    type = 'Mammel' # Class variable

    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]  # instance varoiabel
        else:
            self.name = args[0] 
            self.age = args[1]

        print(args)
    
    def get_name(self):
        return f'{self.name} : {type}'


class Instructor:
    
    def __init__(self, name):
        self.name = name


class Student(Person, Instructor):
    
    def __init__(self, name):
        # super().__init__(name);

        Person.__init__(self, name)
        Instructor.__init__(self, name + 'jhfsdkhfdsj')


