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
        
    def increment_obometer(self, miles):
        self.obometer_reading += miles
    
class battery ():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print (f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.batttery_size == 100:
            range = 315

        print (f"This car can go about {range} miles on a full charge.")

class ElectroCar(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = battery()

my_tesla = ElectroCar('tesla', 'model s', 2019)
