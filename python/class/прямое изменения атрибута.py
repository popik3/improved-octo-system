class car:

    def __init__(self, make, model, year,):
        self.make = make
        self.model = model
        self.year = year
        self.obometer_reading = 0

    def get_discriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_obometer(self):
        print(f"This car has {self.obometer_reading} miles on it")

my_new_car = car('audi', 'A4', '2019',)
print(my_new_car.get_discriptive_name())
"""поменяно"""
my_new_car.obometer_reading = 23

"""поменяно"""
my_new_car.read_obometer()
