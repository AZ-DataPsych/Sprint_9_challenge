'''
These modules provides a class for testing the class and
 generating random numbers inside the class.

 '''
import random


class Product():
    ''' This is a root class that will produce some products'''

    def __init__(
            self,
            name,
            price=10,
            weight=20,
            flammability=0.5,
            identifier=None):
        # Generate a random integer between 100 and 999 (inclusive)

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        '''this func wil check sealability of products'''
        if self.price / self.weight < 0.5:
            return "Not so stealable..."
        elif self.price / self.weight >= 0.5 and self.price / self.weight < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        '''This func will assess the danger of explosion of products'''
        if self.flammability * self.weight < 10:
            return "...fizzle."
        elif (self.flammability * self.weight >= 10
              and self.flammability * self.weight < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    '''This is a child class that will inherit from calss Product'''

    def __init__(
            self,
            name,
            price=10,
            weight=10,
            flammability=0.5,
            identifier=None):
        super().__init__(
            name, price, weight, flammability, identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        '''This func inside the child class that shows example ineritances'''
        if self.weight < 5:
            return "That Tickles"
        elif self.weight >= 5 and self.weight < 15:
            return " Hey that hurt!"
        else:
            return "OUCH"
