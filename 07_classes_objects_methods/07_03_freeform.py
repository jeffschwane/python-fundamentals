'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

class Plant:
    """Models attributes and methods of a plant object.

    ...

    Attributes
    ----------
    name : str
        common name of the plant
    species : str
        latin name of the species of the plant
    color : str
        primary color of the planet
    light : int
        light requirements of the plant (0 - 5), 5 being the highest
    water : int
        water requirments of the plant (0 - 5), 5 being the highest

    Methods
    -------
    __str__(self)
        Prints the planet's name and species.

    __add__(self)
        Add attributes of two instances of that class using the + operator
    """

    def __init__(self, name, species, color, light, water):
        self.name = name
        self.species = species
        self.color = color
        self.light = light
        self.water = water

    def __str__(self):
        return f'The plant is a {self.name} or {self.species}.'

    def __add__(self,other):
        color = self.color + ' and ' + other.color
        return color


s = Plant('Snake plant','Sansiveria','green',2,2)
r = Plant('Rubber plant','Ficus Elastica Tiniki','tan',4,3)
print(s)
print(r)
print(s+r)
s.color = 'green and yellow'
print(s.color)