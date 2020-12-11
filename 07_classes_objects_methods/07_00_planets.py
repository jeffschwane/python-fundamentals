'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    """Models attributes and methods of a planet object.

    ...

    Attributes
    ----------
    name : str
        name of the planet
    size : str
        size of the planet
    color : str
        color of the planet
    position : str
        position from the planet from the sun (1 = closest)

    Methods
    -------
    __str__(self)
        Prints the planet's name, size, color and position from the sun.
    """

    def __init__(self, name, size, color, position):
        self.name = name
        self.size = size
        self.color = color
        self.position = position
    
    def __str__(self):
        return f'{self.name} is a {self.size} {self.color} planet that is the {self.position} planet from the sun.'

e = Planet('Earth','medium','blue/green','third')
print(e)
