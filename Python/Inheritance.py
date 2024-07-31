class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def get_habitat(self):
        print(f'Lives in {self.habitat}')

    def sound(self):
        print('Makes sound')

class Dog(Animal):
    def __init__(self):
        super().__init__('Kennel')

animal = Animal('meh')
animal.get_habitat()

dog = Dog()
dog.sound()
dog.get_habitat()