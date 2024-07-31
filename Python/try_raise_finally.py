class AdultException(Exception):
    pass
    
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def get_minor_age(self):
        if self.age > 18:
            raise AdultException
        else:
            print(self.age)
        
    def display_person(self):
        try:
            self.get_minor_age()
        except AdultException:
            print('This is an adult')
        finally:
            print(self.name)


Person("Dhaval", 23).display_person()
