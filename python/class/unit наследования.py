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

    def update_odometer(self,mileage):
        if mileage >= self.obometer_reading:
            self.obometer_reading = mileage
        else:
            print("You can't roll back an obometer!")

class ElectricCar(car):

    def __init__(self, make, model, year):
        super().__init__(make,model,year)

my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_discriptive_name())