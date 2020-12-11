class Car:
    """Car class with model (car's model, e.g. "Toyota"),
    year (car's manufacturing year , e.g "2000") and
    speed (car's current speed, in km/h).
    """

    def __init__(self, model, year, speed=0):
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        """add 5 to the speed data attribute each time it is called"""
        self.speed += 5

    def brake(self):
        """subtract 5 from the speed data attribute each time it is called.
        The speed should not go below 0, so if brake() is called when the speed
        is already 0, the speed should stay 0
        """
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def honk_horn(self):
        """print {model} goes 'beep beep',
        where {model} is the object's model
        """
        print(f"{self.model} goes 'beep beep'")
