'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

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

class Tree(Plant):
    """Models attributes and methods of a tree object."""

    def __init__(self, name, species, color, light, water, height):
        super().__init__(name, species, color, light, water)
        self.height = height   

class PalmTree(Tree):
    """Models attributes and methods of a palm tree object."""

    def __init__(self, name, species, color, light, water, height, location):
        super().__init__(name, species, color, light, water, height)
        self.location = location

s = Plant('Snake plant','Sansiveria','green',2,2)
r = Plant('Rubber plant','Ficus Elastica Tiniki','tan',4,3)
print(s)
print(r)
print(s+r)
s.color = 'green and yellow'
print(s.color)
p = PalmTree('majestic palm', 'palmiera', 'lush jungle', 5, 5, 30, 'Florida')
print(p.location)