class car():
    def __init__(self, make, model, year,):
        self.make = make
        self.model = model
        self.year = year

    def get_descroptive_name (self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

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

print (my_tesla.get_descroptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()