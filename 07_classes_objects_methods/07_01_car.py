'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    """Models a car.
    
    ...

    Attributes
    ----------
    model : str
        model of the card
    year : int
        year the car was made
    max_speed : int
        maximum speed of the car in mph

    Methods
    -------
    increase_speed()
        Increases the max_speed of the car by 5 when called.
    details()
        Prints the details of the car.
    """
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_speed(self):
        self.max_speed += 5
        print(f'The max speed of the {self.model} has been increased by 5 mph.')

    def details(self):
        print(f'A {self.year} {self.model} capable of reaching a speed of {self.max_speed} mph.')


t = Car('Toyota Corolla',1989,100)
h = Car('Honda Civic Hybrid',2008,120)
t.details()
t.increase_speed()
t.details()
h.details()

